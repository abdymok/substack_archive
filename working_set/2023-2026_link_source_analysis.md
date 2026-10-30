# Archive link-source analysis (2023–2026)

## Scope and method

- Source files: the four annual linked-reference indexes in `working_set/`.
- Link occurrences: 5,438.
- Distinct URL strings: 4,219.
- Distinct source domains: 1.
- Posts represented: 976.
- Classification is domain-based. Known publishers and platforms are normalized through an explicit alias map. Unrecognized domains remain visible as `other / unclassified`, rather than being guessed.
- The dataset retains the original URL, link text, post/day and source domain. No URL is rewritten or deduplicated in the link-level file.
- Category shares use link occurrences as the denominator, not unique articles or unique URLs.

## Annual totals

| Year | Link occurrences | Distinct URLs | Source domains |
|---|---:|---:|---:|
| 2023 | 1248 | 998 | 1 |
| 2024 | 1717 | 1335 | 1 |
| 2025 | 1341 | 1123 | 1 |
| 2026 | 1132 | 951 | 1 |

## Category mix by year

| Category | 2023 | 2024 | 2025 | 2026 | Total |
|---|---:|---:|---:|---:|---:|
| other / unclassified | 1248 | 1717 | 1341 | 1132 | 5438 |

## Leading normalized sources by year

### 2023

| Publisher | Category | Link occurrences | Unique URLs |
|---|---|---:|---:|
| [invalid URL] | other / unclassified | 1248 | 998 |

### 2024

| Publisher | Category | Link occurrences | Unique URLs |
|---|---|---:|---:|
| [invalid URL] | other / unclassified | 1717 | 1335 |

### 2025

| Publisher | Category | Link occurrences | Unique URLs |
|---|---|---:|---:|
| [invalid URL] | other / unclassified | 1341 | 1123 |

### 2026

| Publisher | Category | Link occurrences | Unique URLs |
|---|---|---:|---:|
| [invalid URL] | other / unclassified | 1132 | 951 |

## Classification caveats

- Domain classification is not article-level fact-checking. A link to a news publisher's homepage and a link to one of its articles both count as that publisher.
- Publisher aliases are normalized only where the domain-to-publisher relationship is clear. The registry preserves the original domain so the normalization is auditable.
- Some domains are multi-purpose platforms (notably Google, YouTube and Substack). Their categories describe the platform/domain, not the specific content linked.
- `other / unclassified` is a deliberate holding category for domains not confidently identified. There are 1 such domains, accounting for 5438 link occurrences. They should be reviewed before drawing conclusions from the category mix.
- `unique_posts` counts distinct year + Day identifiers within each source. The source-level dataset is a descriptive index, not a measure of editorial importance or source reliability.

## Files

- `2023-2026_normalized_links.csv`: one row per link occurrence, preserving original context.
- `2023-2026_source_registry.csv`: one row per source domain, with normalized publisher, category and archive-wide counts.
- `2023-2026_source_year.csv`: one row per source domain per year.
- `2023-2026_category_year.csv`: category totals and annual shares.
