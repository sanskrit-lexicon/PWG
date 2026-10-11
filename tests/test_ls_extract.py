"""Smoke tests — make_change3_ls (entry parsing + <ls> citation export).

init_entries() is the shared multi-line entry parser of the pwg_ls2 change
builders: metaline <L>... through <LEND>. make_number_change() rewrites
bare <ls>N, N, N.</ls> citations into attributed <ls n="ABBR"> forms —
the literary-source normalization export. Regex forms verified against
real citation shapes from pwg_ls2 change files.
"""
import pytest
from conftest import FIXTURES, load_module

mc = load_module("make_change3_ls", "pwg_ls2/p/make_change3_ls.py")
ENTRIES = FIXTURES / "pwg_entries_fixture.txt"


@pytest.fixture(autouse=True)
def _reset_entry_ldict():
    """Entry.Ldict is class-level state; the change builders are single-shot
    CLIs that never reset it. Reset between tests so multiple init_entries
    calls in one process behave like separate runs."""
    mc.Entry.Ldict = {}
    yield
    mc.Entry.Ldict = {}


def test_init_entries_parses_fixture():
    recs = mc.init_entries(str(ENTRIES))
    assert len(recs) == 3
    assert [e.metad["L"] for e in recs] == ["1644", "5818", "6938"]
    # 1-based line numbers must bound each entry exactly (metaline..LEND)
    assert (recs[0].linenum1, recs[0].linenum2) == (1, 3)
    assert (recs[2].linenum1, recs[2].linenum2) == (7, 9)
    assert recs[0].lend == "<LEND>"
    assert "gaṇa" in recs[0].datalines[0]


def test_entry_metaline_reuses_parseheadline():
    recs = mc.init_entries(str(ENTRIES))
    assert recs[1].metad["pc"] == "1-0423"
    assert recs[1].metad["k1"] == "arc"


def test_duplicate_L_refused(tmp_path):
    dup = tmp_path / "dup.txt"
    body = ENTRIES.read_text(encoding="utf-8")
    dup.write_text(body + body, encoding="utf-8")  # L 1644 twice
    with pytest.raises(SystemExit):
        mc.init_entries(str(dup))


def test_second_init_entries_in_same_process_is_single_shot():
    """Locked known behavior: Entry.Ldict is class-level and never reset,
    so re-running init_entries over the same file in one process raises
    'duplicate L' (scripts are one-shot per invocation). If this ever
    passes without SystemExit, the shared-state semantics changed."""
    mc.init_entries(str(ENTRIES))
    with pytest.raises(SystemExit):
        mc.init_entries(str(ENTRIES))


def test_number_change_form_three_numbers():
    """<ls>1, 2, 3.</ls> -> fully attributed form, punctuation preserved."""
    got = mc.make_number_change("<ls>1, 2, 3.</ls>", "MBH.", None, None)
    assert got == '<ls n="MBH.">1, 2, 3.</ls>'
    got = mc.make_number_change("<ls>1, 2, 3</ls>", "MBH.", None, None)
    assert got == '<ls n="MBH.">1, 2, 3</ls>'


def test_number_change_form_variant_reading():
    """Real 'v. l.' (varia lectio) tail is carried through."""
    got = mc.make_number_change("<ls>1, 2, 3. v. l.</ls>", "P.", None, None)
    assert got == '<ls n="P.">1, 2, 3. v. l.</ls>'


def test_number_change_form_two_numbers_fills_work_volume():
    """Two-number citation borrows the work's volume (n1) into ls n=."""
    got = mc.make_number_change("<ls>2, 3.</ls>", "ṚV.", "1", None)
    assert got == '<ls n="ṚV. 1,">2, 3.</ls>'


def test_number_change_form_single_number_fills_volume_and_sarga():
    """One-number citation borrows work volume AND sarga (n1, n2)."""
    got = mc.make_number_change("<ls>5.</ls>", "MBH.", "1", "2")
    assert got == '<ls n="MBH. 1, 2,">5.</ls>'
