import csv, json, re, zipfile
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
from html.parser import HTMLParser
from openpyxl import load_workbook

BOOK = Path("1070_posts_with_war_day_fixed.xlsx")
ARCHIVE = Path("substack_archive.zip")
OUT = Path("missing_subtitle_posts.json")

class TextExtractor(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg"}
    def __init__(self):
        super().__init__()
        self.parts=[]
        self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.skip += 1
        if tag in {"p","br","div","li","h1","h2","h3","blockquote"}: self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip: self.skip -= 1
        if tag in {"p","div","li","h1","h2","h3","blockquote"}: self.parts.append("\n")
    def handle_data(self, data):
        if not self.skip:
            s=re.sub(r"\s+"," ",data).strip()
            if s: self.parts.append(s)

def clean_html(raw):
    p=TextExtractor(); p.feed(raw)
    return re.sub(r"\n{2,}","\n", " ".join(p.parts)).strip()

wb=load_workbook(BOOK)
aliases={"date":{"date"},"day":{"day_of_war","day","war_day"},"title":{"title"},"subtitle":{"subtitle"},"url":{"url","canonical_url"}}
ws=cols=header=None
for sh in wb.worksheets:
    for rr in range(1,min(sh.max_row,15)+1):
        found={}
        for cc in range(1,sh.max_column+1):
            k=str(sh.cell(rr,cc).value or "").strip().lower().replace(" ","_")
            for f,names in aliases.items():
                if k in names: found[f]=cc
        if len(found)==5: ws,cols,header=sh,found,rr; break
    if ws: break
if ws is None: raise RuntimeError("Workbook columns not found")

def normdate(v):
    return v.strftime("%Y-%m-%d") if hasattr(v,"strftime") else str(v or "")[:10]

targets=[]
for rr in range(header+1,ws.max_row+1):
    vals={f:ws.cell(rr,c).value for f,c in cols.items()}
    if not str(vals["subtitle"] or "").strip():
        url=str(vals["url"] or "").strip()
        slug=urlparse(url).path.rstrip("/").split("/")[-1]
        targets.append({"row":rr,"date":normdate(vals["date"]),"day":str(vals["day"] or ""),"title":str(vals["title"] or "").strip(),"url":url,"slug":slug})

with zipfile.ZipFile(ARCHIVE) as z:
    names=set(z.namelist())
    posts=list(csv.DictReader(z.open("posts.csv").read().decode("utf-8-sig").splitlines()))
    by_slug={}
    for p in posts:
        pid=p.get("post_id","")
        slug=pid.split(".",1)[1] if "." in pid else ""
        if slug: by_slug.setdefault(slug,[]).append(p)
    for item in targets:
        cand=by_slug.get(item["slug"],[])
        if not cand:
            # fallback to slug substring in archive paths
            cand=[p for p in posts if item["slug"] and item["slug"] in p.get("post_id","")]
        if cand:
            cand.sort(key=lambda p: (p.get("post_date","")[:10] != item["date"], p.get("is_published")!="true"))
            p=cand[0]; item["post_id"]=p.get("post_id","")
            html_candidates=[n for n in names if n.startswith("posts/"+item["post_id"]) and n.endswith(".html")]
            if html_candidates:
                # Prefer exact post ID HTML; exclude metrics and other derivatives.
                html_candidates.sort(key=lambda n:(n.count("."),len(n)))
                item["text"]=clean_html(z.read(html_candidates[0]).decode("utf-8","replace"))[:5000]
            else: item["text"]=""
        else:
            item["post_id"]=""; item["text"]=""

# For October or other records outside the Substack export, look in the repository's 2026 redacted text archive.
md=Path("26_redact.md")
if md.exists():
    raw=md.read_text(encoding="utf-8",errors="replace")
    for item in targets:
        if not item.get("text"):
            # Find the post URL slug or a distinctive day marker and capture a bounded section.
            pats=[re.escape(item["slug"]), re.escape(item["title"])]
            pos=-1
            for pat in pats:
                if pat and len(pat)>3:
                    m=re.search(pat,raw,re.I)
                    if m: pos=m.start(); break
            if pos>=0:
                chunk=raw[pos:pos+7000]
                item["text"]=re.sub(r"\s+"," ",re.sub(r"!\[[^]]*\]\([^)]*\)"," ",chunk)).strip()[:5000]
                item["source"]="26_redact.md"

OUT.write_text(json.dumps({"workbook":BOOK.name,"sheet":ws.title,"header_row":header,"blank_count":len(targets),"posts":targets},ensure_ascii=False,indent=2),encoding="utf-8")
print(f"blank_rows={len(targets)}; with_text={sum(bool(x.get('text','').strip()) for x in targets)}; without_text={sum(not x.get('text','').strip() for x in targets)}")

# Trigger extraction workflow after workflow installation.
