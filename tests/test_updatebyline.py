"""Smoke tests: updateByLine.py — the change-file parse + apply entry point.

Every test uses REAL PWG entry lines / change records from
pwg_ls2/pratishakya/changes_1.txt (see conftest.REAL for provenance).
"""
import pytest

from conftest import REAL, UPDATEBYLINE_COPIES, load_module

OLD_LINE = REAL["ls383217_old"]
NEW_LINE = REAL["ls383217_new"]


def change_text(lnum, old, new):
    return f"{lnum} old {old}\n{lnum} new {new}\n"


def write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return str(p)


def test_change_parses_new_record(updatebyline):
    chg = updatebyline.Change(1, f"383217 old {OLD_LINE}", f"383217 new {NEW_LINE}")
    assert chg.chgcode == "new"
    assert chg.lnumstr == "383217"
    assert chg.oldtext == OLD_LINE
    assert chg.newtext == NEW_LINE


def test_change_parses_ins_and_del(updatebyline):
    ins = updatebyline.Change(2, f"9 old {OLD_LINE}", "9 ins inserted text")
    assert ins.chgcode == "ins" and ins.newtext == "inserted text"
    delrec = updatebyline.Change(3, f"9 old {OLD_LINE}", "9 del ")
    assert delrec.chgcode == "del" and delrec.newtext == ""


def test_change_rejects_line_number_mismatch(updatebyline):
    with pytest.raises(SystemExit):
        updatebyline.Change(1, "383217 old X", "383218 new Y")


def test_change_rejects_missing_change_keyword(updatebyline):
    with pytest.raises(SystemExit):
        updatebyline.Change(1, f"383217 old {OLD_LINE}", "383217 replace Y")


def test_init_changein_skips_comments_and_parses_pairs(updatebyline, tmp_path):
    # Exactly the record shape of a real changes file, with comment lines.
    changein = write(
        tmp_path,
        "changes.txt",
        "; <L>38493<pc>4-0117<k1>nAraka<k2>nAraka\n"
        "; pc = print change\n"
        + change_text(383217, OLD_LINE, NEW_LINE)
        + ";\n"
        + change_text(459319, REAL["ls459319_old"], REAL["ls459319_new"]),
    )
    changes = updatebyline.init_changein(changein)
    assert [c.lnumstr for c in changes] == ["383217", "459319"]
    assert [c.chgcode for c in changes] == ["new", "new"]
    assert changes[0].newtext == NEW_LINE
    assert changes[1].newtext == ""


def test_init_changein_rejects_odd_line_count(updatebyline, tmp_path):
    changein = write(tmp_path, "changes.txt", f"383217 old {OLD_LINE}\n")
    with pytest.raises(SystemExit):
        updatebyline.init_changein(changein)


def entry_file(tmp_path):
    """Real nAraka entry: header line + one real <ls> citation line."""
    lines = [REAL["nAraka_header"], OLD_LINE]
    return write(tmp_path, "in.txt", "\n".join(lines) + "\n")


def test_update_applies_new_replacement(updatebyline, tmp_path):
    fin = entry_file(tmp_path)
    changein = write(tmp_path, "changes.txt", change_text(2, OLD_LINE, NEW_LINE))
    fout = str(tmp_path / "out.txt")
    updatebyline.update(fin, changein, fout)
    out = open(fout, encoding="utf-8").read().splitlines()
    assert out == [REAL["nAraka_header"], NEW_LINE]


def test_update_applies_ins_after_line(updatebyline, tmp_path):
    fin = entry_file(tmp_path)
    changein = write(tmp_path, "changes.txt", "2 old %s\n2 ins %s\n" % (OLD_LINE, REAL["prat_body"]))
    fout = str(tmp_path / "out.txt")
    updatebyline.update(fin, changein, fout)
    out = open(fout, encoding="utf-8").read().splitlines()
    assert out == [REAL["nAraka_header"], OLD_LINE, REAL["prat_body"]]


def test_update_applies_del_removes_line(updatebyline, tmp_path):
    fin = entry_file(tmp_path)
    changein = write(tmp_path, "changes.txt", "2 old %s\n2 del \n" % OLD_LINE)
    fout = str(tmp_path / "out.txt")
    updatebyline.update(fin, changein, fout)
    out = open(fout, encoding="utf-8").read().splitlines()
    assert out == [REAL["nAraka_header"]]


def test_update_refuses_old_text_mismatch(updatebyline, tmp_path):
    # Safety guard: a stale 'old' text must never be applied silently.
    fin = entry_file(tmp_path)
    changein = write(tmp_path, "changes.txt", "2 old totally different line\n2 new X\n")
    with pytest.raises(SystemExit):
        updatebyline.update(fin, changein, str(tmp_path / "out.txt"))


def test_update_refuses_out_of_range_line_number(updatebyline, tmp_path):
    fin = entry_file(tmp_path)
    changein = write(tmp_path, "changes.txt", change_text(999, OLD_LINE, NEW_LINE))
    with pytest.raises(SystemExit):
        updatebyline.update(fin, changein, str(tmp_path / "out.txt"))


def test_update_noop_is_identity(updatebyline, tmp_path):
    fin = entry_file(tmp_path)
    fout = str(tmp_path / "out.txt")
    updatebyline.update(fin, write(tmp_path, "changes.txt", ""), fout)
    assert open(fout, encoding="utf-8").read() == open(fin, encoding="utf-8").read()


def test_all_pwg_ls2_copies_in_sync(tmp_path):
    # Each workdir carries its own updateByLine.py copy (no repo-root copy);
    # they are hand-synced. The copies must apply the same real change
    # record to the same real entry byte-identically. (The 01/ copy is a
    # known benign variant — it prints errors without .encode('utf-8') —
    # so this pins BEHAVIOR, not bytes.)
    fin = write(
        tmp_path,
        "in.txt",
        REAL["nAraka_header"] + "\n" + OLD_LINE + "\n",
    )
    changein = write(tmp_path, "changes.txt", change_text(2, OLD_LINE, NEW_LINE))
    expected = None
    for rel in UPDATEBYLINE_COPIES:
        mod = load_module(rel, name=f"updatebyline_{rel.replace('/', '_')}")
        fout = str(tmp_path / (rel.replace("/", "_") + ".out"))
        mod.update(fin, changein, fout)
        got = open(fout, encoding="utf-8").read()
        if expected is None:
            expected = got
        assert got == expected, f"{rel} applied the record differently"
