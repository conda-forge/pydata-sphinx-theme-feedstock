import shutil
from pathlib import Path
import os
import tempfile

SRC_DIR = Path(os.environ["SRC_DIR"])
PKG_VERSION = os.environ["PKG_VERSION"]

WHL = SRC_DIR / f"pydata_sphinx_theme-{PKG_VERSION}-py3-none-any.whl"

LICENSE_DIR = SRC_DIR / "third-party-licenses"
LICENSE_DIR.mkdir()

LICENSES = {
    "font-awesome-LICENSE.txt": "pydata_sphinx_theme/theme/pydata_sphinx_theme/static/vendor/fontawesome/*/LICENSE.txt"
}

with tempfile.TemporaryDirectory() as td:

    tdp = Path(td)
    ZIP = tdp / f"{WHL.name}.zip"
    DIST = tdp / "dist"
    shutil.copy2(WHL, ZIP)
    shutil.unpack_archive(ZIP, DIST)

    for dest, pattern in LICENSES.items():
        license = next(DIST.glob(pattern))
        shutil.copy2(license, LICENSE_DIR / dest)
