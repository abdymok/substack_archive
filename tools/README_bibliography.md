# Bibliography build

The public bibliography is maintained in the separate `abdymok.github.io` repository. This script reads the audited source-year CSVs in this repository and updates only the public bibliography page and its machine-readable CSV. It does not publish or copy the `working_set` directory.

## Requirements

- Python 3.10 or later
- No third-party packages

## Run locally

Clone both repositories side by side:

```text
projects/
  substack_archive/
  abdymok.github.io/
```

From the `substack_archive` directory:

```bash
python tools/build_bibliography.py --public-dir ../abdymok.github.io/bibliography
```

Optional arguments:

```bash
python tools/build_bibliography.py --public-dir ../abdymok.github.io/bibliography --as-of "November 4, 2026" --coverage-through "October 28" --wayback
```

The script writes `bibliography/entries.csv`, synchronizes the page header total, annual totals, category counts and scope table, and refreshes both HTML working copies. It preserves annotations and representative links.

## Counting rules

- 2021–2022 rows use the explicit `included=1` flag in `2021-2022_source_year.csv`.
- 2023–2026 rows use the two-post threshold in `2023-2026_source_year.csv`; the `personal archive` category is excluded.
- Display category counts combine the underlying source categories using the page's established groupings.
- Platform/service and news-outlet shares are calculated only from link occurrences in qualifying entries. The remaining share consists of reference, research and official-source categories.
- The 2023–2026 source-year CSV does not contain first/last citation dates. For those rows, the build retains the already-audited date ranges from the current page until those dates are added to the data file.

With `--wayback`, the script checks representative links on X/Twitter, Telegram, Facebook and Google Maps against the Internet Archive availability API. It adds an `archived` link only when a snapshot is reported. This lookup requires an internet connection and does not submit pages for archiving.

Review the generated diff before committing or pushing either repository.
