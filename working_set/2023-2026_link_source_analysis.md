# Archive link-source analysis (2023–2026)

## Scope and method

- Link occurrences: **5438**.
- Distinct URL strings: **4218**.
- Original source domains: **854**.
- Normalized publishers: **824**.
- Distinct year/day labels with links: **976**.
- The four-year post index contains 1,070 individual Markdown files. The link-level CSV records archive day and date, not a unique post filename, so source-level `unique_post_days` counts distinct archive day labels, not individual Markdown files.
- Publisher aliases are consolidated in the publisher-level comparison. Original domains and URLs remain in the link-level data for audit.
- Classification is domain-based. Domains not confidently identified remain `other / unclassified`.
- Counts are link occurrences, not unique articles, readership, or influence.
- Six manual review passes have reclassified 751 link occurrences among the most frequently linked domains. The unclassified set has fallen from 587 domains / 1,036 occurrences to **306 occurrences**. Each remaining unclassified domain occurs once.
- Two publisher labels had conflicting row-level categories. They are resolved explicitly: BelTA is state media; Nashi Groshi is Ukrainian media. Original row-level assignments remain visible in `normalized_links.csv`.
- Google Books aliases previously labelled `Google Books / Google` and `Google Books` are now consolidated as `Google Books`.

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
| Ukrainian media | 67 | 130 | 55 | 47 | 299 |
| business / commercial | 27 | 15 | 19 | 25 | 86 |
| news | 434 | 763 | 521 | 283 | 2001 |
| official sources | 43 | 52 | 62 | 47 | 204 |
| other / unclassified | 24 | 110 | 96 | 76 | 306 |
| personal / creative | 14 | 2 | 1 | 0 | 17 |
| personal archive | 248 | 164 | 114 | 295 | 821 |
| reference | 157 | 153 | 185 | 164 | 659 |
| research | 61 | 83 | 55 | 39 | 238 |
| social media | 172 | 245 | 233 | 156 | 806 |
| state media | 1 | 0 | 0 | 0 | 1 |

## Leading normalized publishers by year

### 2023

| Publisher | Category | Links | Unique URLs | Unique post-day labels |
|---|---|---:|---:|---:|
| ukraine@war (Substack) | personal archive | 226 | 165 | 123 |
| The New York Times | news | 103 | 58 | 52 |
| The Washington Post | news | 92 | 47 | 49 |
| Wikipedia | reference | 87 | 83 | 56 |
| YouTube | social media | 47 | 46 | 31 |
| X / Twitter | social media | 45 | 45 | 30 |
| Telegram | social media | 26 | 26 | 24 |
| Reuters | news | 24 | 19 | 16 |
| The Atlantic | news | 24 | 15 | 14 |
| Kyiv Post | Ukrainian media | 21 | 15 | 13 |

### 2024

| Publisher | Category | Links | Unique URLs | Unique post-day labels |
|---|---|---:|---:|---:|
| ukraine@war (Substack) | personal archive | 158 | 127 | 120 |
| The New York Times | news | 147 | 73 | 75 |
| The Washington Post | news | 110 | 40 | 45 |
| Wikipedia | reference | 80 | 76 | 65 |
| Telegram | social media | 68 | 66 | 56 |
| YouTube | social media | 62 | 58 | 45 |
| X / Twitter | social media | 50 | 49 | 40 |
| Financial Times | news | 47 | 22 | 20 |
| Reuters | news | 41 | 37 | 33 |
| The Atlantic | news | 38 | 18 | 16 |

### 2025

| Publisher | Category | Links | Unique URLs | Unique post-day labels |
|---|---|---:|---:|---:|
| ukraine@war (Substack) | personal archive | 108 | 88 | 74 |
| Wikipedia | reference | 95 | 88 | 50 |
| The New York Times | news | 88 | 52 | 51 |
| X / Twitter | social media | 74 | 65 | 38 |
| Telegram | social media | 58 | 56 | 43 |
| YouTube | social media | 55 | 51 | 36 |
| Reuters | news | 42 | 40 | 35 |
| Archive.ph | reference | 35 | 34 | 31 |
| The Atlantic | news | 32 | 10 | 17 |
| The Guardian | news | 32 | 26 | 22 |

### 2026

| Publisher | Category | Links | Unique URLs | Unique post-day labels |
|---|---|---:|---:|---:|
| ukraine@war (Substack) | personal archive | 229 | 192 | 88 |
| YouTube | social media | 86 | 80 | 56 |
| Google | reference | 70 | 69 | 7 |
| The New York Times | news | 65 | 41 | 41 |
| abdymok (GitHub Pages) | personal archive | 54 | 17 | 26 |
| Archive.ph | reference | 36 | 33 | 31 |
| Wikipedia | reference | 28 | 25 | 25 |
| Telegram | social media | 20 | 20 | 19 |
| Reuters | news | 19 | 16 | 15 |
| The Guardian | news | 19 | 14 | 14 |

## Recurring source selection

A publisher is recurring in a year when it appears on at least two distinct archive day labels in that year. Personal-archive sources are excluded. Grouping is by normalized publisher and year, not by publisher + category. This prevents BelTA from being split into two one-off rows and omitted from the recurring-source list.

| Year | Recurring external sources |
|---|---:|
| 2023 | 58 |
| 2024 | 94 |
| 2025 | 100 |
| 2026 | 57 |
| **Total source-year entries** | **309** |

## Classification caveats

- Classification describes the source domain, not the reliability or quality of an individual article.
- Multi-purpose platforms and services are classified by their role as a platform or reference service, not by the content of every linked page.
- Some domains remain unclassified because the link context is insufficient or the site does not fit the current categories. Review continues from the most frequently linked domains downward.
- This is a descriptive source index, not a rating of accuracy, credibility or importance.

## Dataset files

- `2023-2026_normalized_links.csv`: one row per link occurrence with original context and normalized source.
- `2023-2026_source_registry.csv`: one row per original source domain.
- `2023-2026_publisher_registry.csv`: one row per normalized publisher, with resolved category.
- `2023-2026_source_year.csv`: one row per normalized publisher per year, categories no longer split into separate rows.
- `2023-2026_category_year.csv`: category totals and annual shares.
- `2023-2026_recurring_publisher_year_counts.csv`: recurring sources only, including unique URL counts.
