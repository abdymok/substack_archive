# Substack Archive — Work-in-Progress Checkpoint

Last updated: 2026-10-30

## Purpose

Resume the metadata-completion task without repeating earlier research. Complete and audit the 1,070-post workbook, preserving existing corrections and canonical URLs.

## Repository and working file

- Repository: https://github.com/abdymok/substack_archive
- Working workbook: `1070_posts_with_war_day_fixed.xlsx`
- Workbook scope: 1,070 posts; fields include date, day of war, title, subtitle, and URL.
- The workbook was previously committed on the `main` branch.
- Current workbook blob SHA fetched on 2026-10-30: `1a7a38e3e62571151985f8e2294748faf347bd26`.
- This checkpoint is a separate handoff note. It does not replace or modify the workbook.

## Progress at checkpoint

- 190 subtitles were recovered from `posts.csv` and added to the working copy.
- At the last workbook audit, 57 subtitle cells remained blank.
- `posts.csv` is stale and ends on 2026-09-30, so it cannot supply October subtitles.
- The repository also contains `1070_posts_with_war_day.csv`, but it is an older baseline: 1,070 rows and 449 blank subtitle cells. Do not use it to overwrite the fixed workbook or mistake it for the working copy.
- The October listing was supplied by the user and is now recovered through Day 1681. The exact mapping is below.
- The workbook itself has not yet been updated with the October subtitles.

## Complete October subtitle mapping supplied by the user

Apply these to matching existing rows. Match both day and title, preserve the existing URLs and corrected day labels, and keep continuation rows separate.

| Existing row | Subtitle |
|---|---|
| Day 1708 | Load limits |
| Day 1707 | The People on the Land |
| Day 1706 | Oleshky for Election Day |
| Day 1705 | The language of partnership |
| Day 1703 | Z skips the reading list |
| Day 1702 | It was not |
| Day 1701 | 10 days until November |
| Day 1700 | Sun Shines, Door Spins |
| Day 1699 (contd) | Pawn shop with flags |
| Day 1699 | Road to Peremoha |
| Day 1698 | It is Sunday already and I’ve updated the infrastructure page |
| Day 1696 | No subtitle supplied. Leave blank unless independently sourced. |
| Day 1695 | Self-portrait at 6:10 AM, October 15, 2026 |
| Day 1694 (contd) | The Soup is Hot |
| Day 1694 | The man on the corner |
| Day 1693 | An appeal to hypocrisy. |
| Milestone Moment | Momento mori |
| Day 1692 | Exhale, Exfil |
| Day 1691 (contd) | Washington hands Moscow the table |
| Day 1691 | The American Jacket |
| Day 1690 | The arithmetic of absurdity |
| Day 1689 | The only app you need |
| Day 1688 | Обіцянка-цяцянка |
| Day 1687 | Indian summer |
| Day 1686 | Up the creek |
| Day 1685 | Kyiv bridges need no help |
| Day 1684 (contd) | Popcorn chrysanthemums |
| Day 1684 | Botanical gardens |
| Day 1683 | The authentic copy |
| Day 1682 | The thing itself |
| Day 1681 | The map became the neighborhood |

Important distinction: Day 1707's post title is “For White House morons watching Newsmax”; its subtitle is “The People on the Land”. Do not put the title into the subtitle column.

Day 1709 — “Caught in the nets” appeared in the listing, but no canonical URL was supplied and no Day 1709 row exists in the 1,070-row CSV baseline. Do not add it to the workbook until its canonical URL and intended row treatment are verified.

## Rules and cautions

1. Preserve all corrected day labels and existing URLs.
2. Match subtitle entries to existing rows using the post title/day, including separate `contd` entries. Do not collapse continuation posts into their parent post.
3. Do not invent subtitles, URLs, dates, or day numbers.
4. Leave Day 1696 blank unless a reliable source supplies a subtitle.
5. Do not add Day 1709 as a new row until its canonical URL and row treatment are established.
6. Make changes to a working copy and retain the original archive/workbook.
7. After applying October subtitles, audit remaining blanks and verify the row count and URL preservation.
8. Do not use `1070_posts_with_war_day.csv` as the workbook source: it is the older 449-blank baseline, not the fixed 57-blank working copy.

## Resume checklist

- [ ] Obtain a local copy of `1070_posts_with_war_day_fixed.xlsx` for binary spreadsheet editing. The GitHub connector can fetch the workbook as base64, but cannot directly materialize/edit the binary workbook in the current tool path.
- [ ] Apply the complete October subtitle mapping above to the matching workbook rows.
- [ ] Keep Day 1696 blank unless sourced.
- [ ] Verify the Day 1709 canonical URL before considering a row addition.
- [ ] Save and commit the updated workbook under the existing working filename.
- [ ] Re-audit the remaining blanks, row count, and URL preservation.

## Resume prompt

“Read `WORK_IN_PROGRESS.md` in `abdymok/substack_archive`, obtain the current `1070_posts_with_war_day_fixed.xlsx`, and continue from the checkpoint. Do not repeat the 190-subtitle recovery. Apply the complete October subtitle mapping, preserve corrected day labels and existing URLs, keep separate continuation rows, leave Day 1696 blank, and do not add Day 1709 without a verified canonical URL.”
