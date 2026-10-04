"""Shared helpers for the PWG smoke suite (H5799).

Loads the repo's script-style modules by path (they are not packages) and
holds REAL dictionary-entry fixtures lifted from this repo's own files:

- <L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1        (pagecolumn/pwg_page_index.py docstring)
- <L>38493<pc>4-0117<k1>nAraka<k2>nAraka    (pwg_ls2/pratishakya/changes_1.txt)
- <L>46157<pc>4-0793<k1>puruza<k2>pu/ruza   (pwg_ls2/pratishakya/changes_1.txt)
- <L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2  (pwg_ls2/mbh/parseheadline.py)
- change records 383217 / 459319 old+new    (pwg_ls2/pratishakya/changes_1.txt)
"""
import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent


def load_module(relpath, name=None):
    """Import a repo script (top-level functions only) by filesystem path."""
    path = REPO / relpath
    spec = importlib.util.spec_from_file_location(name or path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Real PWG entry/record strings (kept verbatim, trailing spaces included).
REAL = {
    "nAraka_header": "<L>38493<pc>4-0117<k1>nAraka<k2>nAraka",
    "puruza_header": "<L>46157<pc>4-0793<k1>puruza<k2>pu/ruza",
    "aMSa_header": "<L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1",
    "visarga_header": "<L>16850<pc>292-3<k1>visarga<k2>visarga<h>1<e>2",
    # changes_1.txt record 383217: real <ls> correction (trailing space kept).
    "ls383217_old": "<ls>PRĀT. 3, 21</ls> als bedeutungslose Dehnung angesehen wird; vgl. 2. {#yAtanAH#} ",
    "ls383217_new": "<ls>AV. PRĀT. 3, 21</ls> als bedeutungslose Dehnung angesehen wird; vgl. 2. {#yAtanAH#} ",
    # changes_1.txt record 459319: real <ls>VP.</ls> removal (new side empty).
    "ls459319_old": "<ls>VP.</ls> ",
    "ls459319_new": "",
    # Real citation body from the same correction batch.
    "prat_body": "<ls>PRĀT. 3, 118.</ls> <ls>WHITNEY</ls> zu <ls>AV.</ls>",
}

# The seven byte-identical updateByLine.py copies under pwg_ls2/ (hand-synced
# workdir convention; canonical copy = pwg_ls2/ak).
UPDATEBYLINE_COPIES = [
    "pwg_ls2/ak/updateByLine.py",
    "pwg_ls2/01/updateByLine.py",
    "pwg_ls2/mbh1/updateByLine.py",
    "pwg_ls2/lsnum1/updateByLine.py",
    "pwg_ls2/lsunknown/updateByLine.py",
    "pwg_ls2/ramayana0/updateByLine.py",
    "pwg_ls2/RV/updateByLine.py",
]

# The three byte-identical parseheadline.py copies.
PARSEHEADLINE_COPIES = [
    "pwg_ls2/mbh/parseheadline.py",
    "pwg_ls2/av/parseheadline.py",
    "pwg_ls2/ramayana0/parseheadline.py",
]


@pytest.fixture(scope="session")
def updatebyline():
    return load_module("pwg_ls2/ak/updateByLine.py", name="pwg_updatebyline")


@pytest.fixture(scope="session")
def parseheadline():
    return load_module("pwg_ls2/mbh/parseheadline.py", name="pwg_parseheadline")


@pytest.fixture(scope="session")
def page_index():
    return load_module("pagecolumn/pwg_page_index.py", name="pwg_page_index")
