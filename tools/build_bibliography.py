#!/usr/bin/env python3
"""Build the public annotated-bibliography data export and synchronize page counts.

Run from a checkout of substack_archive:
  python tools/build_bibliography.py --public-dir ../abdymok.github.io/bibliography

Inputs are the audited source-year CSVs in working_set. The script preserves
editorial annotations and representative links in index.html while rebuilding
all summary counts, the scope table and the public six-column CSV.
"""
from __future__ import annotations

import argparse
import csv
import html
import re
import json
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "working_set"
YEARS = range(2021, 2027)
GROUPS = {
    "news": "international-news",
    "Ukrainian media": "ukrainian-media",
    "research": "research-and-analysis",
    "official sources": "official-sources",
    "reference": "reference-and-archives",
    "social media": "platforms-services-and-specialist-references",
    "business / commercial": "platforms-services-and-specialist-references",
    "specialist": "platforms-services-and-specialist-references",
    "other / unclassified": "platforms-services-and-specialist-references",
    "personal / creative": "platforms-services-and-specialist-references",
    "state media": "state-media",
}
PLATFORM_CATEGORIES = {
    "social media", "business / commercial", "specialist",
    "other / unclassified", "personal / creative",
}
NEWS_CATEGORIES = {"news", "Ukrainian media", "state media"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def normalized_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for r in read_csv(WORK / "2021-2022_source_year.csv"):
        if r.get("included") != "1":
            continue
        rows.append({
            "year": r["year"], "category": r["category"],
            "publisher": r["normalized_publisher"], "links": r["links"],
            "posts": r["posts"],
            "date_range": f'{r.get("first_cited", "")}–{r.get("last_cited", "")}',
        })
    for r in read_csv(WORK / "2023-2026_source_year.csv"):
        if r.get("year") not in {str(y) for y in range(2023, 2027)}:
            continue
        if r.get("category") == "personal archive" or int(r.get("unique_posts", "0")) < 2:
            continue
        rows.append({
            "year": r["year"], "category": r["category"],
            "publisher": r["normalized_publisher"],
            "links": r["link_occurrences"], "posts": r["unique_posts"],
            # The 2023–2026 source-year CSV does not carry citation dates.
            # The current HTML date ranges are retained below as audited metadata.
            "date_range": "",
        })
    return rows


def current_date_ranges(page: str) -> dict[tuple[str, str], str]:
    """Read existing, audited date ranges before regenerating data-driven counts."""
    ranges: dict[tuple[str, str], str] = {}
    year = None
    for block in re.findall(r'<section class="year" id="year-(20\d{2})">(.*?)(?=<section class="year"|<h2 class="scope-heading">)', page, re.S):
        year, body = block
        for dt in re.findall(r'<dt>(.*?)</dt>', body, re.S):
            name = re.search(r'<i>(.*?)</i>', dt, re.S)
            count = re.search(r'·\s*\d+ posts?\s*·\s*([^<]+)</span>', dt)
            if name and count:
                ranges[(year, html.unescape(re.sub(r"<.*?>", "", name.group(1))))] = html.unescape(count.group(1).strip())
    return ranges


def make_public_csv(rows: list[dict[str, str]], ranges: dict[tuple[str, str], str]) -> str:
    for r in rows:
        if not r["date_range"]:
            r["date_range"] = ranges.get((r["year"], r["publisher"]), "")
    rows.sort(key=lambda r: (int(r["year"]), r["category"].casefold(), -int(r["links"]), r["publisher"].casefold()))
    out = []
    import io
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["year", "category", "publisher", "links", "posts", "date range"])
    for r in rows:
        writer.writerow([r["year"], r["category"], r["publisher"], r["links"], r["posts"], r["date_range"]])
    return stream.getvalue()


def summarize(rows: list[dict[str, str]]) -> dict[str, dict]:
    summary = {}
    for y in YEARS:
        yr = [r for r in rows if r["year"] == str(y)]
        total = sum(int(r["links"]) for r in yr)
        platform = sum(int(r["links"]) for r in yr if r["category"] in PLATFORM_CATEGORIES)
        news = sum(int(r["links"]) for r in yr if r["category"] in NEWS_CATEGORIES)
        top = sorted(yr, key=lambda r: (-int(r["links"]), r["publisher"].casefold()))[:5]
        summary[str(y)] = {
            "entries": len(yr), "total": total,
            "platform_share": 100 * platform / total if total else 0,
            "news_share": 100 * news / total if total else 0,
            "top": top,
        }
    return summary



FRAGILE_HOSTS = {
    "x.com", "www.x.com", "twitter.com", "www.twitter.com",
    "t.me", "www.t.me", "telegram.me", "www.telegram.me",
    "facebook.com", "www.facebook.com", "m.facebook.com", "web.facebook.com",
    "maps.app.goo.gl", "maps.google.com",
}


def add_wayback_links(page: str) -> str:
    """Append an archived link where the Wayback availability API finds a snapshot."""
    def process_references(match):
        content = match.group(2)
        def process_link(link_match):
            href = html.unescape(link_match.group(1))
            host = (urlparse(href).hostname or "").lower()
            is_google_maps = host in {"google.com", "www.google.com"} and urlparse(href).path.startswith("/maps")
            if host not in FRAGILE_HOSTS and not is_google_maps:
                return link_match.group(0)
            tail = content[link_match.end():]
            if re.match(r'\s*<a class="archive-link"', tail):
                return link_match.group(0)
            api = "https://archive.org/wayback/available?" + urlencode({"url": href})
            request = Request(api, headers={"User-Agent": "BibliographySnapshotCheck/1.0"})
            try:
                with urlopen(request, timeout=12) as response:
                    data = json.load(response)
                snapshot = data.get("archived_snapshots", {}).get("closest", {})
                if not snapshot.get("available") or not snapshot.get("url"):
                    return link_match.group(0)
                archived = html.escape(snapshot["url"], quote=True)
                return link_match.group(0) + f' <a class="archive-link" href="{archived}" rel="nofollow">archived</a>'
            except Exception as exc:
                print(f"Wayback lookup skipped for {href}: {exc}")
                return link_match.group(0)
        return match.group(1) + re.sub(r'<a href="([^"]+)">([^<]*)</a>', process_link, content) + match.group(3)
    return re.sub(r'(<p class="references">)(.*?)(</p>)', process_references, page, flags=re.S)


def update_page(page: str, rows: list[dict[str, str]], as_of: str, coverage: str) -> str:
    ranges = current_date_ranges(page)
    # Preserve and restore date ranges as the 2023–2026 source-year table has no dates.
    for r in rows:
        if not r["date_range"]:
            r["date_range"] = ranges.get((r["year"], r["publisher"]), "")
    summary = summarize(rows)
    total_entries = sum(v["entries"] for v in summary.values())

    css = "  .scope-table-wrap { width: 100%; }\n  .scope-table { width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 0.8125rem; line-height: 1.4; }\n  .scope-table th, .scope-table td { text-align: left; vertical-align: top; padding: 0.45rem 0.35rem; border-bottom: 1px solid #e8e8e8; overflow-wrap: anywhere; }\n  .scope-table thead th { font-weight: 600; border-bottom: 1px solid #999; }\n  .scope-table th:nth-child(1) { width: 8%; }\n  .scope-table th:nth-child(2) { width: 9%; }\n  .scope-table th:nth-child(3), .scope-table th:nth-child(4) { width: 16%; }\n  .scope-table th:nth-child(5) { width: 51%; }\n  .method-summary { margin-top: 1rem; }
  .archive-link { font-size: 0.8em; margin-left: 0.2rem; text-decoration-style: dotted; }\n  @media (max-width: 40rem) { .scope-table { font-size: 0.72rem; } .scope-table th, .scope-table td { padding: 0.35rem 0.2rem; } }\n"
    if ".scope-table-wrap" not in page:
        page = page.replace("</style>", css + "\n</style>", 1)
    elif ".archive-link" not in page:
        page = page.replace("</style>", "  .archive-link { font-size: 0.8em; margin-left: 0.2rem; text-decoration-style: dotted; }\n</style>", 1)
    page = re.sub(
        r'<p class="meta">.*?</p>',
        f'<p class="meta">2021–2026 · updated {html.escape(as_of)} · {total_entries} annual publisher entries across six years · 2026 coverage through {html.escape(coverage)}</p>',
        page, count=1, flags=re.S,
    )
    # Rebuild each annual publisher count from the CSV-derived rows.
    for y, data in summary.items():
        pattern = rf'(<section class="year" id="year-{y}">.*?<p class="intro">.*?\d+ recurring external publishers)'
        page, n = re.subn(pattern, lambda m: re.sub(r'\d+ recurring external publishers$', f'{data["entries"]} recurring external publishers', m.group(1)), page, count=1, flags=re.S)
        if n != 1:
            raise ValueError(f"Could not update annual count for {y}")

    # Rebuild category source counts while preserving the existing editorial sentence.
    for y in YEARS:
        for anchor in sorted(set(GROUPS.values())):
            n_sources = sum(1 for r in rows if r["year"] == str(y) and GROUPS.get(r["category"]) == anchor)
            if not n_sources:
                continue
            pattern = rf'(<h3 id="cat-{y}-{re.escape(anchor)}">.*?</h3>\s*<p class="intro">)(.*?)(</p>)'
            def replace_intro(m):
                text = m.group(2)
                # Replace the leading count phrase, retaining any explanatory prose.
                updated, count = re.subn(
                    r'^(?:[A-Za-z-]+|\d+)\s+(?:sources?|publishers?|outlets?),?',
                    f'{n_sources} sources,', text, count=1, flags=re.I,
                )
                if not count:
                    updated = f'{n_sources} sources, ' + text
                return m.group(1) + updated + m.group(3)
            page, _ = re.subn(pattern, replace_intro, page, count=1, flags=re.S)

    # Short methodology summary immediately below the lead, with a link to full notes.
    method = (
        '<p class="intro method-summary">Inclusion requires at least two cited posts in a year. '
        'Direct links to the author’s own archive are excluded; Google redirects are attributed to their resolved destinations. '
        'Counts are link occurrences and distinct posts, not unique articles, readership or influence. The <a href="entries.csv">public CSV</a> lists the annual entries and counts. '
        'The <a href="#method-and-files">full method and file notes</a> explain the rules and source data.</p>'
    )
    if 'class="method-summary"' in page:
        page = re.sub(r'<p class="intro method-summary">.*?</p>', method, page, count=1, flags=re.S)
    else:
        marker = '</p>\n\n<nav id="contents"'
        if marker not in page:
            raise ValueError("Could not locate contents navigation to insert method summary")
        page = page.replace(marker, '</p>\n' + method + '\n<nav id="contents"', 1)

    # A compact scope table: entries, category shares, and five most-linked sources.
    body = ['<h2 class="scope-heading" id="scope">At a glance</h2>',
            '<div class="scope-table-wrap"><table class="scope-table">',
            '<caption>Shares are calculated from link occurrences among qualifying entries. Platforms and services include social media, commercial, specialist and unclassified sources. News outlets include international, Ukrainian and state media. Reference, research and official-source links make up the remainder.</caption>',
            '<thead><tr><th scope="col">Year</th><th scope="col">Entries</th><th scope="col">Platforms and services</th><th scope="col">News outlets</th><th scope="col">Five most-linked sources</th></tr></thead><tbody>']
    for y, d in summary.items():
        names = ' · '.join(f'{html.escape(r["publisher"])} ({int(r["links"]):,})' for r in d["top"])
        body.append(f'<tr><th scope="row">{y}</th><td>{d["entries"]}</td><td>{d["platform_share"]:.1f}%</td><td>{d["news_share"]:.1f}%</td><td>{names}</td></tr>')
    body.append('</tbody></table></div>')
    table = '\n'.join(body)
    if 'id="scope"' in page:
        page = re.sub(r'<h2 class="scope-heading" id="scope">.*?</div>', table, page, count=1, flags=re.S)
    else:
        marker = '<nav id="contents"'
        page = page.replace(marker, table + '\n' + marker, 1)

    page = page.replace('<h2 class="scope-heading">Method and files</h2>',
                        '<h2 class="scope-heading" id="method-and-files">Method and files</h2>')
    return page


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-dir", type=Path, required=True, help="Path to the public bibliography directory")
    parser.add_argument("--as-of", default=date.today().strftime("%B %d, %Y").replace(" 0", " "))
    parser.add_argument("--coverage-through", default="October 28")
    parser.add_argument("--wayback", action="store_true", help="Look up snapshots for fragile representative links")
    args = parser.parse_args()
    page_path = args.public_dir / "index.html"
    if not page_path.exists():
        raise SystemExit(f"Missing public page: {page_path}")
    rows = normalized_rows()
    years = {r["year"] for r in rows}
    if years != {str(y) for y in YEARS}:
        raise SystemExit(f"Unexpected year coverage: {sorted(years)}")
    page = page_path.read_text(encoding="utf-8")
    ranges = current_date_ranges(page)
    csv_text = make_public_csv(rows, ranges)
    page_text = update_page(page, rows, args.as_of, args.coverage_through)
    if args.wayback:
        page_text = add_wayback_links(page_text)
    (args.public_dir / "entries.csv").write_text(csv_text, encoding="utf-8", newline="")
    page_path.write_text(page_text, encoding="utf-8", newline="")
    summary = summarize(rows)
    print(f"Wrote {len(rows)} public entries to entries.csv")
    print("Annual entries: " + ", ".join(f"{y}: {summary[str(y)]['entries']}" for y in YEARS))
    print(f"Total: {sum(v['entries'] for v in summary.values())}")


if __name__ == "__main__":
    main()
