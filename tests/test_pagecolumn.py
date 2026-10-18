"""Smoke tests — pagecolumn/pwg_page_index.py (page/column export views).

Derives the three export views (column / page / reverse) from real PWG
<csl-orig>-style headers. Exercised both at function level (HEADER_RE,
page_of, parse_source) and as the CLI with --src/--outdir on a fixture.
"""
import pytest
from conftest import FIXTURES, load_module, run_py

pi = load_module("pwg_page_index", "pagecolumn/pwg_page_index.py")
HEADERS = FIXTURES / "pwg_headers_fixture.txt"


def test_page_of_two_columns_per_page():
    """PWG prints 2 columns per page; column 1 starts page 1."""
    assert pi.page_of(1) == 1
    assert pi.page_of(2) == 1
    assert pi.page_of(3) == 2
    assert pi.page_of(4) == 2
    assert pi.page_of(119) == 60


def test_parse_source_reads_real_headers_and_breaks():
    entries = pi.parse_source(str(HEADERS))
    assert len(entries) == 3
    aMSa = entries[0]
    assert (aMSa.L, aMSa.vol, aMSa.col, aMSa.k1, aMSa.h) == \
        ("8", 1, 4, "aMSa", "1")
    # entry 1 spans its start column plus the [Page1-0005] break
    assert aMSa.spans == {(1, 4), (1, 5)}
    # entry 3 documents the real float-L Nachtrag form
    sup = entries[2]
    assert sup.L == "26305.290"
    assert sup.spans == {(2, 501), (2, 502)}


def test_header_without_homonym_marker():
    """<h> is optional in real headers."""
    m = pi.HEADER_RE.match("<L>5818<pc>1-0423<k1>arc<k2>arc\n")
    assert m is not None
    L, vol, col, k1, k2, h = m.groups()
    assert (L, vol, col, k1, k2, h) == ("5818", "1", "0423", "arc", "arc", None)


def test_column_and_page_view_strings():
    assert pi.pc_str(1, 4) == "1-0004"
    assert pi.pc_str(12, 3) == "12-0003"


def test_cli_writes_three_views(tmp_path):
    out = tmp_path / "views"
    out.mkdir()
    r = run_py("pagecolumn/pwg_page_index.py",
               ["--src", HEADERS, "--outdir", out])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "parsed 3 PWG entries" in r.stdout
    cols = (out / "pwg_columns.tsv").read_text(encoding="utf-8").splitlines()
    assert cols[0].startswith("column\tvolume\tpage\tn_entries")
    # real row: column 1-0004, volume 1, page 2, headword aMSa
    assert "1-0004\t1\t2\t1\tL8\taMSa" in cols
    pages = (out / "pwg_pages.tsv").read_text(encoding="utf-8").splitlines()
    # column 4 -> physical page 2: page view merges start columns per page
    assert any(line.startswith("1-p0002\t1\t1-0004\t1\tL8")
               for line in pages)
    rev = (out / "pwg_entry_locations.tsv").read_text(encoding="utf-8")
    assert "L26305.290\tsupplement" in rev
