# Archive link-source analysis (2023–2026)

## Scope and method

- Link occurrences: 5438.
- Distinct URL strings: 4219.
- Original source domains: 855.
- Posts represented: 976.
- Publisher aliases are consolidated in the publisher-level comparison. Original domains and URLs remain in the link-level data for audit.
- Classification is domain-based. Domains not confidently identified remain `other / unclassified`.
- Counts are link occurrences, not unique articles or readership.
- Manual review has reclassified 460 link occurrences across the highest-frequency domains. The unclassified set has fallen from 587 domains / 1,036 occurrences to 480 domains / 576 occurrences.

## Annual totals

| Year | Links |
|---|---:|
| 2023 | 1248 |
| 2024 | 1717 |
| 2025 | 1341 |
| 2026 | 1132 |

## Category mix by year

| Category | 2023 | 2024 | 2025 | 2026 | Total |
|---|---:|---:|---:|---:|---:|
| Ukrainian media | 64 | 124 | 53 | 46 | 287 |
| news | 412 | 760 | 515 | 277 | 1964 |
| official sources | 33 | 48 | 56 | 41 | 178 |
| other / unclassified | 138 | 156 | 144 | 138 | 576 |
| personal archive | 243 | 160 | 112 | 294 | 809 |
| reference | 140 | 150 | 180 | 150 | 620 |
| research | 52 | 77 | 49 | 30 | 208 |
| social media | 166 | 242 | 232 | 156 | 796 |

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
| The Guardian | news | 32 | 26 |

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

- Classification describes the source domain, not the reliability or quality of an individual article.
- Multi-purpose platforms and services are classified by their role as a platform or reference service, not by the content of every linked page.
- Some domains remain unclassified because the link context is insufficient or the site does not fit the current categories. Review continues from the most frequently linked domains downward.
- This is a descriptive source index, not a rating of accuracy, credibility or importance.

## Dataset files

- `2023-2026_normalized_links.csv`: one row per link occurrence with original context and normalized source.
- `2023-2026_source_registry.csv`: one row per original source domain.
- `2023-2026_publisher_registry.csv`: one row per normalized publisher.
- `2023-2026_source_year.csv`: one row per normalized publisher per year.
- `2023-2026_category_year.csv`: category totals and annual shares.
