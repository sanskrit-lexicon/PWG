"""Smoke tests — updateByLine (correction-apply engine, parse critical path).

Exercised as the real CLI (python updateByLine.py in changes out) against
real entry lines. The 'new'/'ins'/'del' semantics and the old-text mismatch
refusal are the load-bearing behaviours of every correction batch.
"""
import pytest
from conftest import FIXTURES, REPO, md5, run_py

UPDATE = REPO / "pwg_ls2" / "ak" / "updateByLine.py"
MODERN_COPIES = [
    # byte-identical ins/del-aware group; pwg_ls2/01/updateByLine.py is a
    # deliberate py3-output variant (print(out) vs print(out.encode(...)))
    # and is excluded from the identity lock.
    REPO / "pwg_ls2" / d / "updateByLine.py"
    for d in ("RV", "ak", "lsnum1", "lsunknown", "mbh1", "ramayana0")
]
ENTRIES = FIXTURES / "pwg_entries_fixture.txt"


def lines_of(path):
    return path.read_text(encoding="utf-8").splitlines()


def write_changes(tmp_path, body):
    p = tmp_path / "changes.txt"
    p.write_text(body, encoding="utf-8")
    return p


def test_new_replaces_line(tmp_path):
    """Real change shape from pwg_ls2/p/change_01.txt: trailing comma in
    <ls>...</ls> moved outside the tag, <ls>Sch.</ls> added."""
    old2 = '<ls>P. 1, 1, 14,</ls> gaṇa {#aTarvaveda#} {%ohne Grund%}'
    new2 = '<ls>P. 1, 1, 14</ls>, <ls>Sch.</ls>; gaṇa {#aTarvaveda#} {%ohne Grund%}'
    chg = write_changes(tmp_path, f"2 old {old2}\n2 new {new2}\n")
    out = tmp_path / "out.txt"
    r = run_py(UPDATE, [ENTRIES, chg, out])
    assert r.returncode == 0, r.stdout + r.stderr
    got = lines_of(out)
    assert got[1] == new2
    assert got[0] == lines_of(ENTRIES)[0]  # untouched line stays


def test_ins_inserts_after_line(tmp_path):
    first = lines_of(ENTRIES)[0]
    chg = write_changes(
        tmp_path, f"1 old {first}\n1 ins <note>inserted line</note>\n")
    out = tmp_path / "out.txt"
    r = run_py(UPDATE, [ENTRIES, chg, out])
    assert r.returncode == 0, r.stdout + r.stderr
    got = lines_of(out)
    assert len(got) == len(lines_of(ENTRIES)) + 1
    assert got[1] == "<note>inserted line</note>"
    assert got[2] == lines_of(ENTRIES)[1]  # original line 2 shifted down


def test_del_removes_line(tmp_path):
    third = lines_of(ENTRIES)[2]  # the first <LEND>
    chg = write_changes(tmp_path, f"3 old {third}\n3 del \n")
    out = tmp_path / "out.txt"
    r = run_py(UPDATE, [ENTRIES, chg, out])
    assert r.returncode == 0, r.stdout + r.stderr
    got = lines_of(out)
    assert len(got) == len(lines_of(ENTRIES)) - 1
    assert got[2].startswith("<L>5818")  # next entry's metaline moved up


def test_comment_lines_ignored(tmp_path):
    """';' comments and '---' separators are part of the real convention."""
    first, second, _third, fourth = lines_of(ENTRIES)[:4]
    chg = write_changes(
        tmp_path,
        "; a comment\n"
        f"2 old {second}\n2 del \n"
        ";-----------------\n"
        f"4 old {fourth}\n4 ins X\n",
    )
    out = tmp_path / "out.txt"
    r = run_py(UPDATE, [ENTRIES, chg, out])
    assert r.returncode == 0, r.stdout + r.stderr
    got = lines_of(out)
    assert len(got) == len(lines_of(ENTRIES))  # -1 del, +1 ins
    assert "X" in got[3]


def test_old_text_mismatch_refused(tmp_path):
    """Change citing wrong old-text must fail loudly (exit 1), not corrupt."""
    chg = write_changes(tmp_path, "1 old completely wrong text\n1 new x\n")
    out = tmp_path / "out.txt"
    r = run_py(UPDATE, [ENTRIES, chg, out])
    assert r.returncode == 1
    assert "CHANGE ERROR" in r.stdout or "CHANGE ERROR" in r.stderr


def test_modern_copies_byte_identical():
    """The 6 identical ins/del-aware copies must not drift."""
    digests = {md5(p) for p in MODERN_COPIES}
    assert len(digests) == 1, "updateByLine.py copies have drifted"