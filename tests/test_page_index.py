"""Smoke tests: pagecolumn/pwg_page_index.py — source parse + TSV export views.

Fixture is a mini pwg.txt built from REAL PWG entry headers (see
conftest.REAL provenance) plus a real-shaped [PageV-CCCC] column break.
"""
from conftest import REAL

# Real entries: aMSa (vol 1, col 4, with homonym), nAraka (vol 4, col 117),
# puruza (vol 4, col 793). The [Page1-0005] break marker is the native
# mid-entry column-break shape documented in pwg_page_index.py.
PWG_TXT = "\n".join(
    [
        REAL["aMSa_header"],
        "<ls>AV. 12, 4, 36</ls>",
        "[Page1-0005]",
        "<LEND>",
        REAL["nAraka_header"],
        "<ls>PRĀT. 3, 21</ls>",
        "<LEND>",
        REAL["puruza_header"],
        "<LEND>",
    ]
) + "\n"


def make_src(tmp_path):
    src = tmp_path / "pwg.txt"
    src.write_text(PWG_TXT, encoding="utf-8")
    return str(src)


def test_header_regex_matches_real_headers(page_index):
    m = page_index.HEADER_RE.match(REAL["aMSa_header"])
    assert m.groups() == ("8", "1", "0004", "aMSa", "aMSa", "1")
    m = page_index.HEADER_RE.match(REAL["nAraka_header"])
    assert m.groups() == ("38493", "4", "0117", "nAraka", "nAraka", None)


def test_header_regex_accepts_nachtrag_float_id(page_index):
    # Documented format case (module comment): Nachtrag/supplement records
    # carry a float L-id, e.g. 26305.290; <h> stays optional.
    line = "<L>26305.290<pc>6-1101<k1>nAraka<k2>nAraka"
    m = page_index.HEADER_RE.match(line)
    assert m is not None
    assert m.group(1) == "26305.290"


def test_page_of_is_two_columns_per_page(page_index):
    assert [page_index.page_of(c) for c in (1, 2, 3, 4, 117, 793)] == [
        1, 1, 2, 2, 59, 397,
    ]


def test_pc_str_zero_pads_column(page_index):
    assert page_index.pc_str(1, 4) == "1-0004"
    assert page_index.pc_str(4, 117) == "4-0117"


def test_parse_source_reads_real_entries(page_index, tmp_path):
    entries = page_index.parse_source(make_src(tmp_path))
    assert [e.L for e in entries] == ["8", "38493", "46157"]
    assert [(e.vol, e.col) for e in entries] == [(1, 4), (4, 117), (4, 793)]
    assert [e.k1 for e in entries] == ["aMSa", "nAraka", "puruza"]
    assert entries[0].h == "1" and entries[1].h is None


def test_parse_source_tracks_column_break_spans(page_index, tmp_path):
    entries = page_index.parse_source(make_src(tmp_path))
    # aMSa starts in column 1-0004 and its body breaks into column 1-0005.
    assert entries[0].spans == {(1, 4), (1, 5)}
    assert entries[1].spans == {(4, 117)}


def test_write_column_view_exports_rows(page_index, tmp_path):
    entries = page_index.parse_source(make_src(tmp_path))
    out = str(tmp_path / "cols.tsv")
    n = page_index.write_column_view(entries, out)
    assert n == 3
    lines = open(out, encoding="utf-8").read().splitlines()
    assert lines[0] == "column\tvolume\tpage\tn_entries\tL_ids\theadwords"
    assert "1-0004\t1\t2\t1\tL8\taMSa" in lines
    assert "4-0117\t4\t59\t1\tL38493\tnAraka" in lines


def test_write_page_view_merges_two_columns(page_index, tmp_path):
    entries = page_index.parse_source(make_src(tmp_path))
    # Page view groups by the START column's page: col 4 -> page 2,
    # col 117 -> page 59, col 793 -> 397.
    out = str(tmp_path / "pages.tsv")
    n = page_index.write_page_view(entries, out)
    assert n == 3
    lines = open(out, encoding="utf-8").read().splitlines()
    assert lines[0] == "page\tvolume\tcolumns\tn_entries\tL_ids\theadwords"
    assert "1-p0002\t1\t1-0004\t1\tL8\taMSa" in lines
    assert "4-p0397\t4\t4-0793\t1\tL46157\tpuruza" in lines


def test_write_reverse_view_lists_all_spans(page_index, tmp_path):
    entries = page_index.parse_source(make_src(tmp_path))
    out = str(tmp_path / "reverse.tsv")
    assert page_index.write_reverse_view(entries, out) == 3
    lines = open(out, encoding="utf-8").read().splitlines()
    assert lines[0].startswith("L_id\theadword\thomonym\tvolume\tstart_column")
    amsa = next(l for l in lines if l.startswith("L8\t"))
    assert "1-0004" in amsa and "1-0004,1-0005" in amsa
    naraka = next(l for l in lines if l.startswith("L38493\t"))
    assert "nAraka\t\t4\t4-0117\t4-p0059\t4-0117" in naraka
