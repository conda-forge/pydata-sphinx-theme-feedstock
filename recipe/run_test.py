import sys
from subprocess import call

FAIL_UNDER = 85
COV = ["coverage"]
RUN = ["run", "--source=pydata_sphinx_theme", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "-ra", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "pygments_fallbacks",
    "translations",
    # https://github.com/conda-forge/pydata-sphinx-theme-feedstock/pull/58
    "render_secondary_sidebar_dict",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K, "src/tests"])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
