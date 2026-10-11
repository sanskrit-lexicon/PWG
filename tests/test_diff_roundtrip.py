"""Smoke tests — diff_to_changes + updateByLine round trip.

diff_to_changes.py generates change transactions from an old/new file pair;
its documented contract (module docstring) is that applying them back with
updateByLine reconstructs the new file exactly. That round-trip is the
integrity backbone of every correction batch, so it is a locked property.
"""
from conftest import FIXTURES, REPO, run_py

DIFF = REPO / "pwg_ls2" / "p" / "diff_to_changes.py"
UPDATE = REPO / "pwg_ls2" / "ak" / "updateByLine.py"
ENTRIES = FIXTURES / "pwg_entries_fixture.txt"


def make_new_file(tmp_path):
    """Old file with two real lines edited (ls-tag punctuation moves)."""
    lines = ENTRIES.read_text(encoding="utf-8").splitlines()
    lines[1] = lines[1].replace("<ls>P. 1, 1, 14,</ls>",
                                '<ls>P. 1, 1, 14</ls>, <ls>Sch.</ls>;')
    lines[7] = lines[7].replace("Schluss", "Schluss.")
    new = tmp_path / "new.txt"
    new.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return new, (2, 8)


def test_diff_generates_expected_change_pairs(tmp_path):
    new, changed_lines = make_new_file(tmp_path)
    chg = tmp_path / "changes.txt"
    r = run_py(DIFF, [ENTRIES, new, chg])
    assert r.returncode == 0, r.stdout + r.stderr
    text = chg.read_text(encoding="utf-8")
    for n in changed_lines:
        assert f"{n} old " in text
        assert f"{n} new " in text
    assert ";-----------------" in text  # real separator convention


def test_roundtrip_reconstructs_new_exactly(tmp_path):
    """updateByLine(old, diff(old,new)) == new — the documented contract."""
    new, _ = make_new_file(tmp_path)
    chg = tmp_path / "changes.txt"
    r1 = run_py(DIFF, [ENTRIES, new, chg])
    assert r1.returncode == 0, r1.stdout + r1.stderr
    out = tmp_path / "reconstructed.txt"
    r2 = run_py(UPDATE, [ENTRIES, chg, out])
    assert r2.returncode == 0, r2.stdout + r2.stderr
    assert out.read_text(encoding="utf-8") == new.read_text(encoding="utf-8")


def test_identical_files_yield_no_changes(tmp_path):
    chg = tmp_path / "changes.txt"
    r = run_py(DIFF, [ENTRIES, ENTRIES, chg])
    assert r.returncode == 0, r.stdout + r.stderr
    assert "0 changes written" in r.stdout
    assert chg.read_text(encoding="utf-8") == ""
