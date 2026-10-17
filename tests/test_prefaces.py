"""Smoke tests — prefaces/build_combined.py (front-matter export).

build_combined.py assembles pwgpref_all.{de,en,ru}.md from the 27 per-page
transcriptions. The module runs its build at import time (script style), so
these tests are READ-ONLY: they lock the input contract (all per-page files
present, PAGES table consistent) and the committed outputs' completeness
(all 27 sections present in each language). Byte-identity of regenerated
outputs is deliberately NOT asserted — per-page sources legitimately evolve
between builds.
"""
import ast
import re
from conftest import REPO

PREFACES = REPO / "prefaces"
NN_RE = re.compile(r"^pwgpref(\d\d)\.md$")


def _pages_table():
    """Parse the PAGES list literal without executing the script."""
    tree = ast.parse((PREFACES / "build_combined.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and \
                any(getattr(t, "id", None) == "PAGES" for t in node.targets):
            rows = ast.literal_eval(node.value)
            # rows are (NN, volume, en_label, de_label, ru_label)
            assert all(len(r) == 5 for r in rows), "PAGES rows must be 5-tuples"
            return rows
    raise AssertionError("PAGES table not found in build_combined.py")


def test_pages_table_and_per_page_files_consistent():
    pages = _pages_table()
    assert len(pages) == 27
    on_disk = set()
    for p in PREFACES.glob("pwgpref??.md"):
        m = NN_RE.match(p.name)
        assert m is not None, f"unexpected file {p.name}"
        on_disk.add(m.group(1))
    listed = {r[0] for r in pages}
    assert listed == on_disk, f"table/disk mismatch: {listed ^ on_disk}"
    for nn in listed:
        for suffix in (".md", ".en.md", ".ru.md"):
            assert (PREFACES / f"pwgpref{nn}{suffix}").stat().st_size > 0, \
                f"pwgpref{nn}{suffix} missing or empty"


def test_combined_outputs_cover_all_pages():
    """Each committed combined file carries a section for all 27 pages."""
    markers = {
        "pwgpref_all.de.md": r"^## Seite \d\d — ",
        "pwgpref_all.en.md": r"^## Page \d\d — ",
        "pwgpref_all.ru.md": r"^## Страница \d\d — ",
    }
    for name, pattern in markers.items():
        text = (PREFACES / name).read_text(encoding="utf-8")
        found = re.findall(pattern, text, flags=re.MULTILINE)
        assert len(found) == 27, f"{name}: {len(found)}/27 sections"
        assert re.search(r"(?m)^# ", text), f"{name}: missing H1 title"


def test_combined_outputs_have_toc_and_sources():
    for name, toc in (("pwgpref_all.de.md", "Inhalt"),
                      ("pwgpref_all.en.md", "Contents"),
                      ("pwgpref_all.ru.md", "Содержание")):
        text = (PREFACES / name).read_text(encoding="utf-8")
        assert f"## {toc}" in text, f"{name}: no TOC"
        assert "Source (scan)" in text or "Quelle (Scan)" in text or \
            "Источник (скан)" in text, f"{name}: no scan-source notes"
