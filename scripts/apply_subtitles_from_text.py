import csv, re
from pathlib import Path
from datetime import datetime
from openpyxl import load_workbook

BOOK = Path("1070_posts_with_war_day_fixed.xlsx")
RECOVERY = Path("subtitle_recovery_patch_2026-10-30.csv")
OCTOBER = Path("october_subtitle_patch_2026.csv")

# These 220 subtitles are composed from the archived post bodies.
TEXT_SUBTITLES = {
20:"The sham democracy",
22:"Foreign flaks and photos",
28:"A quiet pause from war",
32:"Radar, missiles, and running",
33:"Running through the missile alert",
34:"The Kinzhal over Kyiv",
47:"TikTok legionnaires",
51:"The Fisherman's market",
69:"Dragon, the parable",
83:"Summer, and F-16s",
93:"The May attack recap",
95:"Ethnonationalism, raids, and war",
97:"After the Kakhovka dam",
101:"Conserve letters: Zaporizhia",
105:"Missiles over Kyiv",
109:"Cobblestones and Prigozhin",
114:"David Petraeus explains Ukraine",
118:"The death of Victoria Amelina",
121:"Five hundred days",
125:"NATO's worst-of-both-worlds",
136:"Belarus, Europe's North Korea",
141:"The imbalance of promises",
143:"Conspicuous consumption",
156:"Cellar labels and politics",
157:"Konstiantynivka, Rostov, and coercion",
164:"The designer's ego",
165:"Biden's empty metaphors",
166:"Photographers in a war zone",
177:"MAGA chaos",
179:"No long-term development scenario",
181:"Mourning beyond borders",
186:"War reporters, still",
200:"Bad haircut, better photographs",
203:"Human error at the top",
204:"The battlefield stalemate",
209:"Living eighteen months ahead",
223:"Soup for depression",
232:"Promises, missiles, and cocktails",
234:"The Senate's Ukraine vote",
237:"Zelenskyy's word salad",
244:"The largest air attack",
248:"Prisoners, borders, and balloons",
251:"Missiles across Ukraine",
252:"Samuel Charap's White House visits",
255:"The economy, measured",
259:"Taiwan's democratic success",
260:"A decade of revolution",
263:"Ten years of war",
264:"41 enemy projectiles",
265:"Phase Three continues",
271:"Zaluzhny, and the rumors",
272:"The commander-in-chief's response",
274:"Imminent is not inevitable",
275:"Mike Johnson's phone calls",
276:"Surveillance of journalists",
277:"Another morning of missiles",
278:"The end of Zaluzhny",
280:"The intelligence committee visits",
284:"Another morning in the metro",
293:"Wagnergate and the CIA",
295:"Mike Johnson's White House meeting",
304:"The Pope's white flag",
305:"The Senate's Ukraine warning",
306:"No demobilization during war",
315:"Moscow's conspiracy theories",
316:"Tsirkon over Kyiv",
317:"Cheap Hokas, expensive war",
323:"Havana Syndrome and Wagnergate",
325:"Havana Syndrome's spy trail",
331:"Mike Johnson treads carefully",
335:"Why Israel gets protection",
336:"Chernihiv and the missing billions",
339:"The cherry blossoms survive",
340:"Johnson's aid vote",
345:"Missiles over Ukraine",
346:"Electronic warfare tested",
348:"The Ocheretyne salient",
349:"Fortifications, blindness, and morale",
350:"Eight hundred days",
357:"Russia pushes toward Kharkiv",
367:"Kyiv Day under fire",
371:"Missiles, F-16s, and sleep",
373:"Electricity rationing returns",
382:"The war's eleventh year",
392:"Prisoners, ammunition, and law",
399:"Yermak's power, Z's voice",
401:"Okhmatdyt under attack",
411:"Biden's decision",
413:"War profiteering at home",
417:"Commanders and discipline",
423:"Kickbacks on fortifications",
439:"Anticipating the next attack",
444:"Pokrovsk and Kursk",
445:"Pokrovsk packs its bags",
447:"Long-range weapons, short leash",
456:"Ukraine's long-range argument",
460:"Crimea under international rule",
464:"Ukraine's failed 2024 mission",
465:"The Victory Plan backfires",
468:"Religion, strategy, and Vance",
472:"AI war lab and energy",
473:"The draft-dodging business",
474:"NATO membership, postponed",
479:"Blackouts and stair-running",
485:"The front keeps moving",
486:"A third plan for war",
496:"Tiger Team's accurate forecast",
509:"Hlukhiv and the missile war",
512:"Russia tests a new missile",
526:"A Christmas list",
530:"The mortar shell scandal",
539:"Missiles over central Kyiv",
540:"Trump's Pentagon picks",
543:"Azerbaijan's downed airliner",
548:"Four systemic failures",
551:"Three questions for strangers",
552:"One in ten absent",
557:"Trump's promises, Kyiv's flattery",
568:"Odesa under ballistic attack",
597:"Truce versus ceasefire",
601:"A Munich moment",
602:"Negotiations and the elephant",
617:"Arsonists recruited online",
619:"Missiles and silence",
620:"Tariffs and conspicuous consumption",
621:"Spring/Summer ukraine@war",
626:"Spring in Kyiv, again",
631:"Little Marco's peace theory",
632:"Signal chats and religious rot",
636:"The finish line, again",
644:"Zvanne bridge, destroyed again",
647:"Parade without invaders",
649:"Russia's imperial roots",
651:"Witkoff's intuition",
652:"Toretsk's rising death toll",
658:"Kyiv's birthday under attack",
664:"Russia's center of gravity",
667:"Three rescuers killed",
668:"Los Angeles, and martial law",
675:"Running and cyber warfare",
678:"NATO summit disappoints",
680:"Bendukidze Lane",
690:"488 more alerts than days",
691:"Whitaker's NATO appointment",
692:"Drone warfare, misunderstood",
693:"Whitaker's star turn",
695:"Dobropillia under attack",
704:"Government ignores advice",
705:"Missiles and foreign correspondents",
706:"Cardboard kids return",
707:"The golden toilet mafia",
708:"Crickets and diplomacy",
710:"53 broken promises",
712:"The Neverland summit",
713:"Alaska, and the ceasefire",
716:"Stabilizing means still fighting",
717:"Gunia Universe opens",
720:"Crimea and Donbas are Ukraine",
732:"Parubiy's assassination",
747:"Putin's four-dimensional chess",
752:"Moldova and Poland's drones",
755:"Russia's eastern dependency",
756:"Lubny under attack",
758:"Tomahawks and red lines",
761:"Maps over cheerful pedagogy",
762:"Kyiv loses power",
763:"A building faces sunrise",
766:"The Kupyansk offensive",
769:"Reconstitution of events",
772:"Air raids and medieval Kyiv",
776:"The absurdist war economy",
778:"Crimea's oil depot",
779:"Energy generation under attack",
781:"Withdraw from Pokrovsk",
783:"Russian casualties, New York art",
786:"Blackouts are not normal",
792:"Variables, scope, persistence",
794:"The anti-corruption investigation",
797:"Miami's peace circus",
798:"Witkoff's Moscow butt dial",
799:"Thanksgiving and Tushino",
801:"Yermak under investigation",
802:"Witkoff and Kushner in Moscow",
803:"November's air defense totals",
805:"Operation Midas detectives",
806:"Putin wants all of Donbas",
807:"Europe's civilizational erasure",
808:"The open society's unfinished business",
809:"The peace plan nobody read",
810:"The window has closed",
811:"Kyiv goes dark",
815:"Europe's ninety-billion loan",
819:"The twenty-point plan",
820:"Odesa's cold winter",
821:"A fragment of the argument",
824:"Vyshhorod, Minsk, and resilience",
825:"A year to forget",
826:"Causation and presidential rhetoric",
827:"Kharkiv, and a new chief",
828:"Budanov takes the office",
834:"Lviv's IRBM and dawn patrol",
835:"Pink, birds, and Lincoln",
838:"Woodpeckers and misplaced meaning",
841:"Kyiv's heat and power",
848:"Lukashenko's birthday message",
853:"Irish monks and Kyiv's heat",
854:"A hundred days ahead",
874:"Missiles and the Paris summit",
875:"The coincidences have tail numbers",
878:"Strategy documents, execution absent",
887:"The Paton Bridge may fall",
908:"Promotion as verdict",
912:"A week before lilacs",
918:"The pattern beneath chaos",
924:"Mindich and Umerov recordings",
929:"Evacuate Kyiv, Zakharova says",
935:"Palantir visits Kyiv",
948:"Zircon over Ukrainian cities",
961:"A pawn shop with flags",
969:"Balush and the archive"
}

# Existing published subtitles that exceed the requested five-word limit.
SHORT_SOURCE = {
836:"Heating plant, fauna, flora",
846:"Groundhog Day, starting with Z",
850:"Sirens are not snooze buttons",
856:"Kyiv's winter, badly managed",
864:"Logic and the missing story",
884:"The boys and the mirror",
885:"Cards, chess, clowns",
902:"Naming things plainly",
915:"A pattern explaining too much",
951:"Alders, raptors, war jacket",
965:"A preamble to the archive",
967:"The eagle in the mail",
974:"The alcoholic's vest",
979:"Twenty-five days to fix",
988:"700,000 words to Gemini",
993:"A ride on my lap",
1005:"Russia fires, Ukraine counts",
1038:"A drone brings a friend",
1039:"Ukraine, Z, and the ducks"
}
SHORT_OCTOBER = {
1059:"Self-portrait at 6:10 AM",
1061:"Infrastructure page updated"
}
NO_WORDS = {262,355,356,746,822,942,1060}

def word_count(s):
    return len(re.findall(r"[\\w’'-]+", s, flags=re.UNICODE))

wb=load_workbook(BOOK)
aliases={"date":{"date"},"day":{"day_of_war","day","war_day"},"title":{"title"},"subtitle":{"subtitle"},"url":{"url","canonical_url"}}
ws=cols=header=None
for sh in wb.worksheets:
    for rr in range(1,min(sh.max_row,15)+1):
        found={}
        for cc in range(1,sh.max_column+1):
            key=str(sh.cell(rr,cc).value or "").strip().lower().replace(" ","_")
            for f,names in aliases.items():
                if key in names: found[f]=cc
        if len(found)==5: ws,cols,header=sh,found,rr; break
    if ws: break
if ws is None: raise RuntimeError("Required workbook columns not found")

def normdate(v):
    return v.strftime("%Y-%m-%d") if hasattr(v,"strftime") else str(v or "")[:10]
def normday(v):
    try: return str(int(v))
    except: return str(v or "").strip()
def rowkey(rr):
    return (normdate(ws.cell(rr,cols["date"]).value),normday(ws.cell(rr,cols["day"]).value),
            str(ws.cell(rr,cols["title"]).value or "").strip(),str(ws.cell(rr,cols["url"]).value or "").strip())

filled={}
# Recover exact published subtitles, with concise replacements where needed.
with RECOVERY.open(encoding="utf-8-sig",newline="") as f:
    for item in csv.DictReader(f):
        rr=int(item["workbook_row"])
        subtitle=SHORT_SOURCE.get(rr,item["recovered_subtitle"].strip())
        filled[rr]=subtitle

# Day 400 was verified against the redacted 2023 archive.
filled[49]="Metaphysical theme park"

# Apply the user-supplied October subtitles, keeping Day 1696 blank and skipping the new Day 1709 row.
with OCTOBER.open(encoding="utf-8-sig",newline="") as f:
    for item in csv.DictReader(f,delimiter=";"):
        if item["action"]!="update": continue
        key=(item["date"],item["day_of_war"],item["title"].strip(),item["url"])
        hits=[rr for rr in range(header+1,ws.max_row+1) if rowkey(rr)==key]
        if len(hits)!=1: raise RuntimeError(f"October match count {len(hits)} for {key}")
        rr=hits[0]
        if item["action"]=="intentional_blank": continue
        filled[rr]=SHORT_OCTOBER.get(rr,item["subtitle"].strip())

# Add concise subtitles composed from the post text.
for rr,subtitle in TEXT_SUBTITLES.items():
    if rr in filled: raise RuntimeError(f"Duplicate subtitle mapping for row {rr}")
    filled[rr]=subtitle

# Never write into an existing subtitle cell; never replace a nonblank value.
for rr,subtitle in sorted(filled.items()):
    if not subtitle.strip(): raise RuntimeError(f"Empty subtitle mapping at row {rr}")
    if word_count(subtitle)>5: raise RuntimeError(f"More than five words at row {rr}: {subtitle!r}")
    cell=ws.cell(rr,cols["subtitle"])
    if str(cell.value or "").strip():
        raise RuntimeError(f"Refusing to overwrite existing subtitle at row {rr}: {cell.value!r}")
    cell.value=subtitle

# Confirm that the only blank cells are the six posts without substantive words and Day 1696.
remaining=[]
for rr in range(header+1,ws.max_row+1):
    if not str(ws.cell(rr,cols["subtitle"]).value or "").strip():
        remaining.append(rr)
if set(remaining)!=NO_WORDS:
    raise RuntimeError(f"Unexpected remaining blanks: {remaining}")
if len(filled)!=442:
    raise RuntimeError(f"Expected 442 fills, got {len(filled)}")
wb.save(BOOK)

audit=[
"# Subtitle completion audit — 2026-10-30",
"",
f"- Workbook: `{BOOK.name}`",
f"- Worksheet: `{ws.title}`",
f"- Data rows: {ws.max_row-header}",
f"- Blank subtitle cells at start: 449",
f"- Subtitles filled: {len(filled)}",
f"- Blank cells retained: {len(remaining)}",
"- Every new subtitle is five words or fewer.",
"- Existing nonblank subtitles were not overwritten.",
"- Day 1696 remains intentionally blank.",
"- Six other posts with no substantive words remain blank.",
"- Day 1709 was not added; this task only filled existing rows.",
"",
"## Rows intentionally left blank",
""
]+[f"- Row {rr}: {rowkey(rr)[0]} · Day {rowkey(rr)[1]} · {rowkey(rr)[2]}" for rr in remaining]+[""]
Path("SUBTITLE_COMPLETION_AUDIT_2026-10-30.md").write_text("\n".join(audit),encoding="utf-8")
print(f"rows={ws.max_row-header}; filled={len(filled)}; blanks={remaining}; max_words={max(word_count(x) for x in filled.values())}")

# Trigger workbook update workflow after installation.
