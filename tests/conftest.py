"""H5799 smoke-test bootstrap — shared helpers.

Fixture provenance (real PWG data, not synthetic):
- L-numbers aTarvaveda (L1644, pc 1-0119), arc (L5818, pc 1-0423), aSoka
  (L6938, pc 1-0514): real entry metalines from pwg_ls2/mbh/change_01.txt.
- <L>8<pc>1-0004<k1>aMSa<k2>aMSa<h>1: real csl-orig/v02/pwg/pwg.txt header,
  as documented in pagecolumn/pwg_page_index.py.
- <L>26305.290: real float-L Nachtrag form documented in pwg_page_index.py.
- <ls>P. 1, 1, 14,</ls> and body fragments: real correction content from
  pwg_ls2/p/change_01.txt.

Legacy directories (misc/, pwg_ls/, pwg_ls1/, pwgissues/, verbs01*) are
excluded per the standing CI convention (ruff.toml).
"""
import hashlib
import importlib.util
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def load_module(name, relpath):
    """Load a repo script as a module without installing it as a package."""
    path = REPO / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, f"cannot load {path}"
    mod = importlib.util.module_from_spec(spec)
    # sibling imports (e.g. make_change3_ls imports parseheadline) resolve
    # against the script's own directory, matching how the scripts are run.
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.remove(str(path.parent))
    return mod


def run_py(script, args, cwd=None):
    """Run a repo script as a real subprocess (CLI entry point)."""
    return subprocess.run(
        [sys.executable, str(script)] + [str(a) for a in args],
        capture_output=True, text=True, cwd=cwd,
    )


def md5(path):
    return hashlib.md5(Path(path).read_bytes()).hexdigest()
