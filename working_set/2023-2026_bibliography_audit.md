# 2023–2026 annotated bibliography: audit and continuation checkpoint

**Status:** consolidated source-level HTML draft saved in `working_set/2023-2026_annotated_bibliography.html`.

## Scope and selection rule

A publisher/source is included in a given year when it appears in **two or more posts** in that year. Links to the author's own archive and sites (the `personal archive` category in the source-year table) are excluded. The same publisher may appear in multiple annual sections because each section describes its use in that year.

The combined annual link files contain:

- 5,438 link occurrences
- 4,219 distinct URL strings
- 855 original source domains
- 976 posts with at least one link
- 820 links classified as personal archive, excluded from the external-source bibliography

Counts are link occurrences and distinct posts, not unique articles, readership, or influence. Inclusion is not an endorsement or a reliability rating.

## Annual entry counts

| Year | Recurring external publishers | Category breakdown |
|---|---:|---|
| 2023 | 57 | 21 international news; 8 Ukrainian media; 5 research; 5 official; 8 reference; 10 social media and other |
| 2024 | 94 | 42 international news; 14 Ukrainian media; 10 research; 8 official; 8 reference; 12 social media and other |
| 2025 | 100 | 46 international news; 10 Ukrainian media; 6 research; 12 official; 12 reference; 14 social media and other |
| 2026 to Oct. 28 | 57 | 28 international news; 8 Ukrainian media; 3 research; 4 official; 5 reference; 9 social media and other |
| **Total annual entries** | **308** | A publisher recurring in more than one year appears once in each relevant year. |

The 2023 categories and annotations are retained from the original HTML template. The 2024–2026 entries use the normalized source registry and the same six broad headings.

## Current HTML draft

- `working_set/2023-2026_annotated_bibliography.html`
- Latest HTML commit: `2c805624b5c9ce3dc602b2874f1c169d56322d17`
- Verified: 308 entries; 57 / 94 / 100 / 57 by year; 22 opening and closing section tags; no empty example links.
- The 2024–2026 entries include link counts, post counts, date spans and representative links.
- The 2024–2026 sections now have source-specific opening descriptions rather than the repeated generic “News publisher” sentence. The 2024 section had four remaining instances of that boilerplate; the 2025 section had 46 and the 2026 section had 28. Those 78 descriptions were rewritten to identify the publication or platform and its relevant editorial or institutional character, while retaining the existing year-specific examples and use notes. This is a cleanup of the publisher-level annotations, not a claim that every entry has been fully checked against every cited post.

### 2024 editorial pass: first seven batches

Updated the 2024 section with post-level annotations for 40 additional external publishers across five batches, bringing the number of enriched entries in that year to 68. The new notes cover The Washington Post, CNN, Financial Times, Bloomberg, Foreign Affairs, ZN.ua, POLITICO Europe, the Office of the President of Ukraine, Ukrainska Pravda, Interfax-Ukraine, Censor.NET, DeepStateMap, the Institute for the Study of War and the Kyiv International Institute of Sociology, NATO, DTEK, the Ukraine Recovery Conference, the White House, United24, Ukraine.ua, the U.S. Department of Defense, Just Security, America First Policy Institute, Ukraine Economic Outlook, Munich Security Conference, the Royal United Services Institute, the Council on Foreign Relations, the Poetry Foundation, Ukrinform, Kyiv Post, The New Voice of Ukraine, Defense Express, Ekonomichna Pravda, Suspilne, The Kyiv Independent, Babel, Texty.org.ua and TSN.

The pass sampled the individual 2024 Markdown posts, including Days 675, 679, 681, 695, 696, 707, 715, 716, 723, 724, 743, 755, 756, 761, 765, 766, 771, 776, 779, 785, 799, 818, 820, 821, 824, 830, 839, 843, 847, 849, 852, 861, 866, 876, 883, 884, 897, 900, 903, 904, 910, 924, 936, 944, 948, 953, 957, 958, 959, 973, 986, 993, 995, 1001, 1008, 1009, 1010, 1021 and 1029. The source-level descriptions now distinguish reporting, official statements, survey evidence, operational mapping, energy-system notices, policy advocacy, think-tank analysis, literary references, reference tools and AI-search use, and note when the archive disputes a source rather than endorsing it.

**Citation issue flagged:** Day 681 (January 5, 2024) describes a link as a *Washington Post* story about Ukrainian marines east of the Dnipro, but the hyperlink points to a `wsj.com` URL whose slug concerns Russian plans to buy Iranian ballistic missiles. The bibliography flags this mismatch. Do not silently repair the link without checking the original source.


**Self-link correction:** The three 2024 URLs previously grouped under the generic Substack label all resolve to the author's own `abdymok.substack.com` posts titled “Setting the Plate Clear”. They were reclassified as personal archive in `2023-2026_source_year.csv`, merged into the 2024 `ukraine@war (Substack)` row, and removed from the external bibliography. The 2024 external-publisher count first fell from 96 to 95 after the self-link correction. The remaining one-off TinyURL entry was then excluded under the two-post rule, leaving 94 recurring external publishers. The category-year table moves three occurrences from social media to personal archive. The raw `open.substack.com` domain remains classified as a platform in the all-years domain registry because it also carries other authors' links in other years.


**Additional 2024 short-link correction:** One of the two links recorded under `tinyurl.com` points to the author's own Day 947 comment and has been moved into personal archive. The remaining TinyURL is labelled “NV” in the July 5 post, but its destination could not be verified. It remains a one-off in the source-year data and is excluded from the recurring-publisher bibliography because it appears in only one post.

## 2026 archive correction

The 2026 linked-reference file covers **January 1–October 28, 2026**, with 1,132 link records across 218 post-day labels. The aggregate `working_set/26_redact.md` file is empty, but the individual post files are available in `working_set/posts/2026/` (247 Markdown files, through October 28). The earlier 2026 draft's statement that the post texts were unavailable was therefore too broad.

## Source files

Primary data in `working_set/`:

- `2023_linked_references.csv`
- `2024_linked_references.csv`
- `2025_linked_references.csv`
- `2026_linked_references.csv`
- `2023-2026_source_year.csv`
- `2023-2026_source_registry.csv`
- `2023-2026_publisher_registry.csv`
- `2023-2026_category_year.csv`
- `2023-2026_link_source_analysis.md`
- `2023-2026_normalized_links.csv`

The four existing annual Markdown files (`2023_annotated_bibliography.md` through `2026_annotated_bibliography.md`) are separate, more selective article-level research notes. The consolidated HTML is the source/publisher-level bibliography modeled on the 2023 HTML template.

## Next editorial pass

1. Enrich the remaining 2024–2026 entries with post-level context, especially recurring Ukrainian media, official sources, research organizations and social accounts.
2. Review the `other / unclassified` entries and publisher labels that still appear as raw domains.
3. Check representative links and dates for obvious redirects, archive copies and label/title mismatches.
4. Update the 2026 section when the archive and linked-reference data are extended beyond October 28.


## Editorial progress checkpoint — 31 October 2026

The consolidated HTML was updated after the earlier audit checkpoint.

- Latest HTML commit: `2c805624b5c9ce3dc602b2874f1c169d56322d17`.
- Latest HTML content SHA: `19f7faddf6b39ff5258baac022fd3717bd755b26`.
- Recounted the HTML sections: 57 entries (2023), 94 (2024), 100 (2025), and 57 (2026); 308 annual entries in total.
- Checked all four sections for the repeated generic news-publisher opening. None remain.
- Rewrote 46 such openings in 2025 and 28 in 2026, and removed the last four in 2024. The new openings distinguish newsrooms, wire services, political publications, broadcasters, aggregators, specialist publications, advocacy outlets and independent projects. Existing link examples and year-specific notes were retained.
- 2023's original 57 entries remain unchanged.

### Remaining work

1. Do a substantive post-level pass over 2025 and 2026. The publisher descriptions are now less formulaic, but selected examples and link labels still need checking against the individual posts, particularly where a link may be critical, ironic, incidental or merely an attribution.
2. Review category assignments. Some sources currently grouped under “international news” are not newsrooms (for example, podcast, lifestyle, running and media-monitoring sites); state media and advocacy outlets may also deserve distinct treatment. Do not silently preserve a mistaken category merely because it appears in the registry.
3. Review raw-domain publisher names and aliases, including whether a platform or host is being mistaken for the originating publisher.
4. Audit representative links, date spans, counts and title/URL mismatches.
5. Re-run the count and structural checks after editorial changes, then prepare a rendered browser preview.
