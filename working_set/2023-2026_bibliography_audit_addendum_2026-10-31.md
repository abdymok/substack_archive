# Bibliography audit addendum — 31 October 2026

This addendum supersedes earlier progress counts in `2023-2026_bibliography_audit.md` where they conflict with the current QA checkpoint. It preserves the original audit history rather than rewriting it.

## Current verified state

- Working branch: `bibliography-qa-2026-10-31`. No changes have been merged to `main` or deployed.
- Main bibliography: 309 recurring source-year entries (58 in 2023, 94 in 2024, 100 in 2025, 57 in 2026).
- All-years appendix: 819 one-day source-year entries, representing 938 link occurrences. The 306 one-off unclassified domains are included for later domain review.
- Recurring platform/pointer index: 19 source-year entries covering Google, Google Books, Perplexity, Amazon, bit.ly, TinyURL, Archive.ph, Tootsie Club and Google NotebookLM. These remain included in the 309 recurring-source total.
- Archive.ph attribution ledger: 71 occurrences, 51 high-confidence, 19 provisional and 1 unresolved (Day 1135). Day 1447 is attributed to the Financial Times; Day 1517 is attributed to The Atlantic. Day 1133's intended NYT source is identified, but its Archive.ph destination resolves to an unrelated Bloomberg capture.
- Post-level anomaly review: 21 grouped cases, 18 reviewed/preserved and 3 open: Day 440ish, Day 1121 (NYT label / BBC URL), and Day 1133 (NYT title / Bloomberg capture).
- Day 1042 Axios annotation corrected to December 30, 2024, following the date displayed on the publisher page. The exact original publication time was not exposed in the accessible page text.
- Day 1121's March 20 Kyiv date is supported by the NYT article's March 19, 2025 update at 7:45 p.m. ET (March 20, 02:45 in Kyiv). The canonical NYT URL remains unverified, so the BBC destination has not been replaced with a guessed URL.
- Reader-facing HTML cleanup: internal audit phrases and correction-history wording removed; generic “linked item” anchors replaced; known tracking parameters stripped; Kyiv Independent/Musk attribution corrected. The 2024 Der Spiegel and RUSI representative links now point to articles rather than homepages.

## Remaining work

1. Review the 19 provisional Archive.ph attributions and resolve the Day 1135 Susan Crawford item. Correct the Day 1133 destination mismatch only after recovering the canonical NYT URL.
2. Finish timestamp checks for Day 775 (Washington Post original versus update date), Day 843 (POLITICO), Day 1108 (NYT café story), Day 1205 (NYT McConnell story), and Day 1373 (The Economist). Day 1042 Axios is annotated December 30; exact time remains unavailable.
3. Recover the canonical NYT destination for Day 1121. Do not guess or insert a reconstructed URL.
4. Obtain author confirmation on the Day 440ish label versus its Day 400 slug and numeric metadata.
5. Continue the 110 unresolved Z-substitution candidates individually. Do not use global replacement.
6. Complete the remaining domain/source-classification review and any necessary editorial annotation improvements.
7. Inspect the rendered bibliography and appendix in a desktop and mobile browser. Source-level CSS checks are not a substitute for rendered QA.
8. Review the draft pull request. Merge and deployment remain deferred until the above work is complete.

## Current working files

- `2023-2026_bibliography_qa_2026-10-31.md`
- `2023-2026_archive_ph_attribution.csv`
- `2023-2026_publication_date_review_remaining.csv`
- `2023-2026_post_level_anomaly_review.csv`
- `2023-2026_annotated_bibliography.html`
- `2023-2026_all_years_appendix.html`
- `2023-2026_all_years_single_day_sources.csv`


## Z-substitution update

Two further canonical URLs were verified against Washington Post publisher pages and restored in the Day 425 and Day 446 post copies, 2023 linked-reference CSV, normalized link dataset and Z review queue. The queue now records 9 verified cases and 106 candidates still pending. No global replacement was used.


Day 440ish clarification: the NYT date correction concerns the separate May 9, 2023 Day 440ish post. Its footnote was corrected from March 28 to March 25 and the malformed NYT homepage URL was replaced with the verified article URL. The March 30 Day 440ish label/slug mismatch remains open as a separate author-confirmation question.


Day 501: verified and restored the Hurst publisher URL for *The Zelensky Effect* in the post copy, annual linked-reference CSV, normalized link dataset, Z review queue and one-day-source appendix.


## Link reconciliation

The annual linked-reference CSVs and normalized dataset match exactly: 5,438 link occurrences and 5,050 distinct day-plus-URL pairs, with zero missing or extra pairs. Recomputed recurring counts match the HTML (58, 94, 100, 57; 309 total). The one-day appendix matches all 819 one-day source-year groups, with zero missing or extra records.


Day 647: restored the AP canonical Zelenskyy article URL and exact headline in the post copy, 2023 linked-reference CSV, normalized link dataset and Z review queue.


Day 574: restored the canonical New York Times article title and URL and corrected the annotation from June 20 to September 19, 2023. The post, annual linked-reference CSV, normalized dataset, date ledger and Z review queue are synchronized.


Day 620: restored the Kyiv Independent canonical URL for its August 11, 2023 report. Post, annual CSV, normalized dataset and Z queue are synchronized.
