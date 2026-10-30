# Archive link-source analysis (2023–2026)

## Scope and method

- Link occurrences: 5438.
- Distinct URL strings: 4219.
- Distinct source domains: 855.
- Posts represented: 976.
- Publisher aliases are consolidated in the publisher-level comparison (for example, `nyt.com` + `nytimes.com`, `wapo.st` + `washingtonpost.com`, and `twitter.com` + `x.com`). Original domains remain in the domain registry and link-level data.
- Classification is domain-based. Unrecognized domains remain `other / unclassified`.
- Counts are link occurrences, not unique articles or readership.

## Annual totals

| Year | Links | Distinct URLs | Source domains |
|---|---:|---:|---:|
| 2023 | 1248 | 998 | 289 |
| 2024 | 1717 | 1335 | 347 |
| 2025 | 1341 | 1123 | 303 |
| 2026 | 1132 | 951 | 264 |

## Category mix by year

| Category | 2023 | 2024 | 2025 | 2026 | Total |
|---|---:|---:|---:|---:|---:|
| personal archive | 232 | 158 | 108 | 283 | 781 |
| other / unclassified | 237 | 334 | 271 | 194 | 1036 |
| social media | 146 | 227 | 225 | 151 | 749 |
| Ukrainian media | 56 | 102 | 43 | 38 | 239 |
| news | 386 | 701 | 457 | 261 | 1805 |
| reference | 124 | 126 | 159 | 139 | 548 |
| official sources | 29 | 34 | 45 | 39 | 147 |
| research | 38 | 35 | 33 | 27 | 133 |

## Leading normalized publishers by year

### 2023

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 226 | 165 |
| The New York Times | news | 102 | 58 |
| The Washington Post | news | 92 | 47 |
| Wikipedia | reference | 87 | 83 |
| YouTube | social media | 47 | 46 |
| X / Twitter | social media | 45 | 45 |
| Telegram | social media | 26 | 26 |
| The Atlantic | news | 24 | 15 |
| Reuters | news | 23 | 18 |
| Kyiv Post | Ukrainian media | 21 | 15 |

### 2024

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 158 | 127 |
| The New York Times | news | 147 | 73 |
| The Washington Post | news | 110 | 40 |
| Wikipedia | reference | 80 | 76 |
| Telegram | social media | 68 | 66 |
| YouTube | social media | 62 | 58 |
| X / Twitter | social media | 50 | 49 |
| Financial Times | news | 47 | 22 |
| Reuters | news | 41 | 37 |
| The Atlantic | news | 38 | 18 |

### 2025

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 108 | 88 |
| Wikipedia | reference | 95 | 88 |
| The New York Times | news | 88 | 52 |
| X / Twitter | social media | 74 | 65 |
| Telegram | social media | 58 | 56 |
| YouTube | social media | 55 | 51 |
| Reuters | news | 42 | 40 |
| Archive.ph | reference | 35 | 34 |
| The Atlantic | news | 32 | 10 |
| The Guardian | news | 29 | 25 |

### 2026

| Publisher | Category | Links | Unique URLs |
|---|---|---:|---:|
| ukraine@war (Substack) | personal archive | 229 | 192 |
| YouTube | social media | 86 | 80 |
| Google | reference | 70 | 69 |
| The New York Times | news | 65 | 41 |
| abdymok (GitHub Pages) | personal archive | 54 | 17 |
| Archive.ph | reference | 36 | 33 |
| Wikipedia | reference | 28 | 25 |
| Telegram | social media | 20 | 20 |
| Reuters | news | 19 | 16 |
| The Guardian | news | 19 | 14 |

## Classification caveats

- Publisher aliases are normalized only where the mapping is reasonably clear. Original domains are retained for audit.
- Multi-purpose platforms such as Google, YouTube and Substack are classified by domain, not by the specific content of each page.
- Unclassified domains: 586 publishers/domains, 1036 link occurrences. These should be reviewed before drawing strong conclusions about category proportions.
- This is a descriptive source index, not a rating of accuracy, credibility or importance.

## Dataset files

- `2023-2026_normalized_links.csv`: one row per link occurrence with original context and normalized source.
- `2023-2026_source_registry.csv`: one row per original source domain.
- `2023-2026_publisher_registry.csv`: one row per normalized publisher.
- `2023-2026_source_year.csv`: one row per normalized publisher per year.
- `2023-2026_category_year.csv`: category totals and annual shares.
