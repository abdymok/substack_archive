# Archive link-source analysis (2023–2026)

## Scope and method

- Link occurrences: 5438.
- Distinct URL strings: 4218.
- Original source domains: 854.
- Posts represented: 976.
- Publisher aliases are consolidated in the publisher-level comparison. Original domains and URLs remain in the link-level data for audit.
- Classification is domain-based. Domains not confidently identified remain `other / unclassified`.
- Counts are link occurrences, not unique articles or readership.
- Six manual review passes have reclassified 751 link occurrences among the most frequently linked domains. The unclassified set has fallen from 587 domains / 1,036 occurrences to 306 domains / 306 occurrences. The remaining set is almost entirely single-occurrence domains.

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
| business / commercial | 26 | 13 | 14 | 23 | 76 |
| news | 431 | 761 | 519 | 279 | 1990 |
| official sources | 43 | 51 | 60 | 47 | 201 |
| other / unclassified | 31 | 130 | 109 | 87 | 357 |
| personal / creative | 14 | 2 | 0 | 0 | 16 |
| personal archive | 248 | 164 | 114 | 295 | 821 |
| reference | 156 | 150 | 185 | 163 | 654 |
| research | 61 | 78 | 53 | 36 | 228 |
| social media | 170 | 242 | 232 | 156 | 800 |
| state media | 1 | 0 | 0 | 0 | 1 |
| Ukrainian media | 67 | 126 | 55 | 46 | 294 |

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
| Reuters | news | 24 | 19 |
| The Atlantic | news | 24 | 15 |
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
