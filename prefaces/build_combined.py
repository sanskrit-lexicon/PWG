#!/usr/bin/env python3
# Build consolidated single-file editions (German / English / Russian) of the
# PWG front matter from the per-page pwgprefNN.* transcriptions/translations.
# Run from the prefaces/ directory:  python build_combined.py
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

HERE = os.path.dirname(os.path.abspath(__file__))

# NN, volume, (en_label, de_label, ru_label)
PAGES = [
    ("01", 1, "Title, vol. 1 (Die Vocale, 1855)", "Titelblatt, Band 1 (Die Vocale, 1855)", "Титульный лист, том 1 (гласные, 1855)"),
    ("02", 1, "Foreword, 1", "Vorwort, 1", "Предисловие, 1"),
    ("03", 1, "Foreword, 2", "Vorwort, 2", "Предисловие, 2"),
    ("04", 1, "Foreword, 3", "Vorwort, 3", "Предисловие, 3"),
    ("05", 1, "Foreword, 4", "Vorwort, 4", "Предисловие, 4"),
    ("06", 1, "Foreword, 5", "Vorwort, 5", "Предисловие, 5"),
    ("07", 1, "Abbreviations, 1", "Abkürzungen, 1", "Сокращения, 1"),
    ("08", 1, "Abbreviations, 2", "Abkürzungen, 2", "Сокращения, 2"),
    ("09", 1, "Abbreviations, 3", "Abkürzungen, 3", "Сокращения, 3"),
    ("10", 1, "Abbreviations, 4", "Abkürzungen, 4", "Сокращения, 4"),
    ("11", 1, "Abbreviations, 5", "Abkürzungen, 5", "Сокращения, 5"),
    ("12", 2, "Title, vol. 2", "Titelblatt, Band 2", "Титульный лист, том 2"),
    ("13", 2, "Addenda to vol. 1", "Nachträge zu Band 1", "Дополнения к тому 1"),
    ("14", 2, "Addenda to vol. 2", "Nachträge zu Band 2", "Дополнения к тому 2"),
    ("15", 2, "Foreword, vol. 2", "Vorwort, Band 2", "Предисловие, том 2"),
    ("16", 2, "Abbreviations, vol. 2 (additions)", "Abkürzungen, Band 2 (Zusätze)", "Сокращения, том 2 (дополнения)"),
    ("17", 3, "Title, vol. 3", "Titelblatt, Band 3", "Титульный лист, том 3"),
    ("18", 3, "Foreword, vol. 3", "Vorwort, Band 3", "Предисловие, том 3"),
    ("19", 3, "Abbreviations, vol. 3 (additions)", "Abkürzungen, Band 3 (Zusätze)", "Сокращения, том 3 (дополнения)"),
    ("20", 4, "Title, vol. 4", "Titelblatt, Band 4", "Титульный лист, том 4"),
    ("21", 4, "Foreword, vol. 4", "Vorwort, Band 4", "Предисловие, том 4"),
    ("22", 5, "Title, vol. 5", "Titelblatt, Band 5", "Титульный лист, том 5"),
    ("23", 5, "Foreword, vol. 5 (part 1)", "Vorwort, Band 5 (Teil 1)", "Предисловие, том 5 (часть 1)"),
    ("24", 5, "Foreword, vol. 5 (part 2)", "Vorwort, Band 5 (Teil 2)", "Предисловие, том 5 (часть 2)"),
    ("25", 6, "Title, vol. 6", "Titelblatt, Band 6", "Титульный лист, том 6"),
    ("26", 7, "Title, vol. 7", "Titelblatt, Band 7", "Титульный лист, том 7"),
    ("27", 7, "Foreword, vol. 7 (final)", "Vorwort, Band 7 (Schluss)", "Предисловие, том 7 (заключительное)"),
]

# language -> (file suffix, output name, doc title, page-word, vol-word, label index)
LANGS = {
    "de": (".md",    "pwgpref_all.de.md",
           "Sanskrit-Wörterbuch (Böhtlingk & Roth) — Vorspann, vollständig (Deutsch)",
           "Seite", "Band", 3,
           "OCR-Transkription des gesamten Vorspanns (Titelblätter, Vorworte, Abkürzungsverzeichnisse, Nachträge) des *Sanskrit-Wörterbuchs* (Otto Böhtlingk & Rudolph Roth, St. Petersburg 1855–1875), in der ursprünglichen Orthographie."),
    "en": (".en.md", "pwgpref_all.en.md",
           "Sanskrit-Wörterbuch (Böhtlingk & Roth) — Front Matter, complete (English)",
           "Page", "vol.", 2,
           "English translation of the complete front matter (title pages, forewords, abbreviation lists, addenda) of the *Sanskrit-Wörterbuch* (Otto Böhtlingk & Rudolph Roth, St. Petersburg 1855–1875)."),
    "ru": (".ru.md", "pwgpref_all.ru.md",
           "Sanskrit-Wörterbuch (Бётлингк и Рот) — предварительные материалы, полностью (русский)",
           "Страница", "том", 4,
           "Русский перевод всех предварительных материалов (титульные листы, предисловия, списки сокращений, дополнения) *Санскритского словаря* (Отто Бётлингк и Рудольф Рот, С.-Петербург, 1855–1875)."),
}

TOC_WORD = {"de": "Inhalt", "en": "Contents", "ru": "Содержание"}
SRC_WORD = {"de": "Quelle (Scan)", "en": "Source (scan)", "ru": "Источник (скан)"}

def strip_page(text):
    """Remove the opening YAML block and the first H1 heading; return (meta, body)."""
    meta = {}
    lines = text.splitlines()
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            m = re.match(r"\s*([A-Za-z_]+):\s*(.*)$", lines[i])
            if m:
                meta[m.group(1)] = m.group(2).strip()
            i += 1
        i += 1  # skip closing ---
    # skip leading blanks
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    # drop the first H1 heading line if present
    if i < len(lines) and lines[i].lstrip().startswith("# "):
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    body = "\n".join(lines[i:]).rstrip()
    return meta, body

def slug(s):
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s.strip())
    return s

for lang, (suf, outname, title, pageword, volword, labidx, intro) in LANGS.items():
    out = []
    out.append(f"# {title}\n")
    out.append(intro + "\n")
    out.append(f"Source index: [README.md](README.md). Per-page files: `pwgprefNN{suf}`.\n")
    # TOC
    out.append(f"## {TOC_WORD[lang]}\n")
    headings = []
    for nn, vol, *labels in PAGES:
        label = labels[labidx - 2]  # labidx 2->en(idx0),3->de(idx1),4->ru(idx2)
        htext = f"{pageword} {nn} — {label}"
        headings.append((nn, htext))
        out.append(f"- [{htext}](#{slug(htext)})")
    out.append("")
    # body
    for nn, vol, *labels in PAGES:
        label = labels[labidx - 2]
        src = os.path.join(HERE, f"pwgpref{nn}{suf}")
        with open(src, encoding="utf-8") as f:
            meta, body = strip_page(f.read())
        htext = f"{pageword} {nn} — {label}"
        scan = meta.get("source_scan", "")
        url = meta.get("source_url", "")
        # demote any in-body headings one level so the page heading stays top (H2)
        body = re.sub(r"(?m)^(#{1,5})(\s)", r"#\1\2", body)
        out.append("\n---\n")
        out.append(f"## {htext}\n")
        if scan or url:
            out.append(f"<sub>{SRC_WORD[lang]}: [{scan}]({url})</sub>\n")
        out.append(body + "\n")
    with open(os.path.join(HERE, outname), "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")
    print(f"wrote {outname}")
