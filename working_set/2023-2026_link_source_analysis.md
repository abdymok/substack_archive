# Archive link-source analysis (2023–2026)

## Scope and method

- Link occurrences: 5438.
- Distinct URL strings: 4219.
- Distinct source domains: 855.
- Distinct post/day records represented: 976.
- Classification is domain-based. Known publisher aliases are normalized, while original domains and URLs are retained.
- Unrecognized domains remain in `other / unclassified`. No attempt is made to infer the content of an unknown site.
- Counts represent link occurrences, not unique articles, readership or editorial weight.

## Annual totals

| Year | Link occurrences | Distinct URLs | Source domains |
|---|---:|---:|---:|
| 2023 | 1248 | 998 | 289 |
| 2024 | 1717 | 1335 | 347 |
| 2025 | 1341 | 1123 | 303 |
| 2026 | 1132 | 951 | 264 |

## Category mix by year

| Category | 2023 | 2024 | 2025 | 2026 | Total |
|---|---:|---:|---:|---:|
| news | 386 | 701 | 457 | 261 | 1805 |
| other / unclassified | 237 | 334 | 271 | 194 | 1036 |
| personal archive | 232 | 158 | 108 | 283 | 781 |
| social media | 146 | 227 | 225 | 151 | 749 |
| reference | 124 | 126 | 159 | 139 | 548 |
| Ukrainian media | 56 | 102 | 43 | 38 | 239 |
| official sources | 29 | 34 | 45 | 39 | 147 |
| research | 38 | 35 | 33 | 27 | 133 |

## Leading normalized sources by year

### 2023

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 226 | 165 |
| Wikipedia | reference | 87 | 83 |
| The New York Times | news | 75 | 57 |
| The Washington Post | news | 65 | 46 |
| YouTube | social media | 46 | 45 |
| X / Twitter | social media | 45 | 45 |
| The New York Times | news | 27 | 1 |
| The Washington Post | news | 27 | 1 |
| Telegram | social media | 26 | 26 |
| The Atlantic | news | 24 | 15 |

### 2024

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 158 | 127 |
| The New York Times | news | 87 | 72 |
| Wikipedia | reference | 80 | 76 |
| Telegram | social media | 68 | 66 |
| YouTube | social media | 62 | 58 |
| The New York Times | news | 60 | 1 |
| The Washington Post | news | 56 | 2 |
| The Washington Post | news | 54 | 38 |
| Financial Times | news | 47 | 22 |
| Reuters | news | 41 | 37 |

### 2025

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 108 | 88 |
| Wikipedia | reference | 95 | 88 |
| X / Twitter | social media | 74 | 65 |
| Telegram | social media | 58 | 56 |
| The New York Times | news | 57 | 51 |
| YouTube | social media | 55 | 51 |
| Reuters | news | 42 | 40 |
| Archive.ph | reference | 35 | 34 |
| The Atlantic | news | 32 | 10 |
| The New York Times | news | 31 | 1 |

### 2026

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 229 | 192 |
| YouTube | social media | 86 | 80 |
| Google | reference | 70 | 69 |
| abdymok (GitHub Pages) | personal archive | 54 | 17 |
| The New York Times | news | 49 | 40 |
| Archive.ph | reference | 36 | 33 |
| Wikipedia | reference | 28 | 25 |
| Telegram | social media | 20 | 20 |
| Reuters | news | 19 | 16 |
| The Guardian | news | 19 | 14 |

## Classification caveats

- Publisher aliases are normalized only where the mapping is clear. The source registry preserves the original domain for audit.
- Multi-purpose services (Google, YouTube, Substack) are classified by platform/domain, not by the specific content of each linked page.
- `other / unclassified` contains 587 domains and 1036 link occurrences. Review these before making strong claims about category proportions.
- The source-level dataset is descriptive. It does not assess accuracy, credibility or importance.

## Dataset files

- `2023-2026_normalized_links.csv`: one row per link occurrence with original context and normalized source.
- `2023-2026_source_registry.csv`: one row per source domain with archive-wide counts.
- `2023-2026_source_year.csv`: one row per source domain per year.
- `2023-2026_category_year.csv`: category totals and annual shares.
