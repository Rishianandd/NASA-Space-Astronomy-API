# TP 2 --- Student Report: Modern Python Tooling & Live API Systems

**Student Name:** Rishi Anand\
**EPITA Login:** `rishi.anand` *(verify this is the exact login required
by EPITA)*\
**Assigned API Group:** Group 5 --- Space & Astronomy\
**Date:** 01/11/2026\
**TestPyPI Live Package URL:**
https://test.pypi.org/project/epita-rishi-anand-space-astronomy/

------------------------------------------------------------------------

## Step 0: Assigned Group Verification

-   **Group Command Output:** Not captured in the terminal evidence
    shared during this work. Run the exact group-verification command
    supplied by the professor and paste its output here before
    submission.
-   **Assigned Domain:** Group 5 --- Space & Astronomy.
-   **Project Directory Name:** The working directory used was
    `E:\Nasa`. The published package name is
    `epita-rishi-anand-space-astronomy`. Confirm whether the professor
    requires the directory itself to be named `epita_<login>_<domain>`.

------------------------------------------------------------------------

## Part 1: Environment Isolation with `uv`

### 1. Comparison of `sys.executable` & `sys.prefix`

**Global Python output:**

``` text
Executable: C:\Program Files\Python312\python.exe
Prefix: C:\Program Files\Python312
```

**`uv` environment output:**

``` text
Executable: E:\Nasa\.venv\Scripts\python.exe
Prefix: E:\Nasa\.venv
```

**Analysis:**

The global Python interpreter runs from the system-wide Python
installation, while `uv run` executes Python using the project's
isolated virtual environment at `E:\Nasa\.venv`. This keeps project
dependencies separate from globally installed packages and other
projects. `uv run` automatically selects and synchronizes the project's
environment, so manually activating the virtual environment is not
necessary.

------------------------------------------------------------------------

## Part 2: Live API Connection & 12-Factor Secret Hygiene

### 1. Git Status Output

The following evidence was collected:

``` text
E:\Nasa>git check-ignore -v .env
.gitignore:1:.env       .env

E:\Nasa>git ls-files .env.template
.env.template
```

A later `git status --short --ignored` showed `.env` as ignored:

``` text
!! .env
!! .venv/
!! __pycache__/
!! dist/
!! nasa/__pycache__/
```

This confirms that `.env` is ignored and `.env.template` is tracked. The
`.env` file was not staged or pushed.

### 2. Live API Response (Redacted)

A live NASA Astronomy Picture of the Day response was received. The API
key was not included in the output.

``` json
{
  "status": "LIVE_SUCCESS",
  "date": "2026-11-01",
  "title": "Colors of the Moon",
  "media_type": "image",
  "image_url": "https://assets.science.nasa.gov/dynamicimage/assets/science/cds/apod/apod/2026/november/MoonColors_Pace_960.jpg?w=960&h=991&fit=clip&crop=faces%2Cfocalpoint",
  "api_key_exposed": false
}
```

### 3. Security Analysis

**Why are environment variables preferable to configuration files such
as `config.json` or `settings.yaml`?**

1.  Secrets can be supplied separately for development, testing, and
    production without changing application source files.
2.  Configuration files are easily committed or shared accidentally.
    Environment variables can instead be injected by the runtime or
    deployment environment, reducing the risk of exposing credentials in
    source control.

**Why are default fallbacks such as `os.getenv("API_KEY", "default")`
dangerous for production secrets?**

A fallback can silently allow the application to continue with an
invalid or insecure value when the required secret is missing. This
hides configuration errors and can cause unexpected production
behaviour. A required production secret should be validated explicitly,
and the application should fail clearly if it is absent.

------------------------------------------------------------------------

## Part 3: Dependency Hygiene & Semantic Versioning

### 1. Dependency Tree (`uv tree`)

The observed dependency tree was:

``` text
Resolved 35 packages in 4ms
epita-rishi-anand-space-astronomy v0.1.0
├── python-dotenv v1.2.4
├── requests v2.34.2
│   ├── certifi v2026.10.23
│   ├── charset-normalizer v3.5.2
│   ├── idna v3.20
│   └── urllib3 v2.8.0
├── hatchling v1.33.0 (group: dev)
│   ├── packaging v26.3
│   ├── pathspec v1.1.1
│   ├── pluggy v1.7.0
│   ├── tomlkit v0.15.2
│   └── trove-classifiers v2026.9.21.13
└── twine v7.0.0 (group: dev)
    ├── id v1.6.1
    │   └── urllib3 v2.8.0
    ├── keyring v25.7.0
    │   ├── jaraco-classes v3.4.0
    │   │   └── more-itertools v11.2.1
    │   ├── jaraco-context v6.1.2
    │   ├── jaraco-functools v4.6.0
    │   │   └── more-itertools v11.2.1
    │   └── pywin32-ctypes v0.2.3
    ├── packaging v26.3
    ├── readme-renderer v46.0
    │   ├── docutils v0.23
    │   ├── nh3 v0.3.7
    │   └── pygments v2.21.0
    ├── requests v2.34.2 (*)
    ├── requests-toolbelt v1.0.0
    │   └── requests v2.34.2 (*)
    ├── rfc3986 v2.0.0
    ├── rich v15.0.0
    │   ├── markdown-it-py v4.2.0
    │   │   └── mdurl v0.1.2
    │   └── pygments v2.21.0
    └── urllib3 v2.8.0
(*) Package tree already displayed
```

**Direct dependencies:**

-   `requests` --- used to make HTTP requests to the API.
-   `python-dotenv` --- loads environment variables from `.env`.

**Development dependencies:**

-   `hatchling` --- builds the Python package.
-   `twine` --- validates and uploads package distributions.

**Transitive dependencies pulled in by `requests` / `rich`:**

-   `requests` pulls in `certifi`, `charset-normalizer`, `idna`, and
    `urllib3`.
-   `rich` pulls in `markdown-it-py` and `pygments`; `markdown-it-py`
    pulls in `mdurl`.
-   In this project tree, `rich` is brought in through the development
    dependency `twine`, rather than being a direct project dependency.

### 2. Lockfile & SemVer Analysis

**Meaning of version specifiers:**

-   `requests = "^2.31.0"`: Under caret-version semantics, permits
    compatible versions from `2.31.0` up to, but not including, `3.0.0`.
-   `urllib3 = "~=2.2.1"`: Permits compatible versions from `2.2.1` up
    to, but not including, `2.3.0`.
-   `rich = "==13.7.1"`: Requires exactly version `13.7.1`.

These are the assignment's version-specifier examples. The project's
actual `pyproject.toml` uses `>=` requirements, not these three example
specifiers.

**If an upstream author releases `3.0.0`, will `^2.31.0` install it? Why
or why not?**

No. The caret requirement limits compatible versions to the 2.x
major-version series, so `3.0.0` is outside the permitted range.

**Fundamental difference between `pyproject.toml` and `uv.lock`:**

`pyproject.toml` declares the project's direct dependencies and
acceptable version requirements. `uv.lock` records the exact resolved
versions of the full dependency graph, including transitive
dependencies, so installations can be reproduced consistently.

**How do SHA-256 hashes in `uv.lock` help protect against supply-chain
attacks?**

The lockfile records hashes for package artifacts. During installation,
the package manager can compare the downloaded artifact's calculated
hash with the expected hash. A mismatch can reveal that the artifact
differs from the one recorded in the lockfile, helping detect tampering
or unexpected package changes.

------------------------------------------------------------------------

## Part 4: Package Build & TestPyPI Deployment

### 1. TestPyPI Deployment Details

-   **TestPyPI Package Name:** `epita-rishi-anand-space-astronomy`
-   **Published Version:** `0.1.0`
-   **Public URL:**
    https://test.pypi.org/project/epita-rishi-anand-space-astronomy/

Both distributions were built successfully:

``` text
Successfully built dist\epita_rishi_anand_space_astronomy-0.1.0.tar.gz
Successfully built dist\epita_rishi_anand_space_astronomy-0.1.0-py3-none-any.whl
```

Both distributions passed `twine check` without warnings after the
README was populated:

``` text
Checking dist\epita_rishi_anand_space_astronomy-0.1.0-py3-none-any.whl: PASSED
Checking dist\epita_rishi_anand_space_astronomy-0.1.0.tar.gz: PASSED
```

The TestPyPI release page showed both the `.whl` and `.tar.gz` files for
version `0.1.0`.

**CLI installation and execution command:**

``` cmd
uv run --no-project --with epita-rishi-anand-space-astronomy --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ epita-rishi-anand-cli
```

**Observed execution output (excerpt):**

``` text
Connecting to NASA API...

NASA ASTRONOMY PICTURE OF THE DAY
----------------------------------
Title: Colors of the Moon
Date: 2026-11-01

Image URL: https://assets.science.nasa.gov/dynamicimage/assets/science/cds/apod/apod/2026/november/MoonColors_Pace_960.jpg?w=960&h=991&fit=clip&crop=faces%2Cfocalpoint
```

The command installed the published package from TestPyPI and
successfully executed its registered CLI entry point, which retrieved
live NASA APOD data.

### 2. Packaging Theory

**Difference between an sdist (`.tar.gz`) and a wheel (`.whl`):**

An sdist is a source archive containing the package's source files and
build metadata. A wheel is a built distribution that can be installed
directly by a compatible installer.

**Why are wheels generally faster and safer to install on client
machines?**

A wheel is already built, so installation generally avoids running the
package's build process on the client machine. This makes installation
faster and reduces the need for local build tools and build-time
execution. Wheels are also validated distribution artifacts with
metadata and recorded compatibility information.

------------------------------------------------------------------------

## Part 5: Professional Debugging Challenge (No `print()`!)

**Important scope note:** The professor's original debugging challenge
source file was not available during this work. A separate practice
file, `scripts/debug_challenge.py`, was created to practise the same
concepts and reproduce the numerical target output. The following
observations and fix are from that practice exercise, not from the
professor's original source. Confirm with the professor whether this
practice exercise is acceptable for the required Part 5 evidence.

### 1. Root Cause Analysis

-   **Observed runtime type of `record['volume']`:** `str` (example
    value `"100"`).
-   **Observed runtime type of `record['weight']`:** `str` (example
    value `"5"`).

Python raised a `TypeError` when the code attempted to compare a string
value with an integer in `if weight > 10`. The API-like input values
were strings, but the calculation expected numeric values. Explicit
conversion to `float` during parsing corrected the type mismatch.

### 2. Call Stack Inspection

At the breakpoint in `compute_weighted_metric`, the observed call
sequence was:

``` text
Frame 1: compute_weighted_metric() — line 14
Frame 2: aggregate_telemetry() — line 28
Frame 3: <module> / main program — line 51
```

The debugger's local variables showed `volume = '100'` and
`weight = '5'`.

### 3. The Fix (Practice Code)

The practice fix converted the incoming values to floats in
`parse_api_record`:

``` python
def parse_api_record(record):
    """Parse an API record."""
    return {
        "volume": float(record["volume"]),
        "weight": float(record["weight"])
    }
```

The practice input records and metric function were then adjusted to
reproduce the numerical target provided in the assignment. This
reproduces the expected output but is not verified as the intended fix
for the professor's original challenge.

### 4. Verified Practice Execution Output

``` text
$ uv run python scripts/debug_challenge.py
Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}
```

------------------------------------------------------------------------

## Submission Checklist

- [x] Global Python and `uv` interpreter paths captured.
- [x] `.env` ignore rule verified.
- [x] `.env.template` tracking verified.
- [x] Live NASA API response captured with no API key exposed.
- [x] `uv tree` captured and analysed.
- [x] Lockfile hash evidence inspected.
- [x] Source distribution and wheel built.
- [x] Both distributions passed `twine check`.
- [x] Both distributions published to TestPyPI and visible on the release page.
- [x] Published CLI installed and executed successfully.
- [x] Missing assigned-group verification evidence identified for follow-up.
- [x] Project directory naming requirement flagged for confirmation.
- [x] Part 5 limitation disclosed: the practice debugging exercise was used because the professor's original challenge file was unavailable.

**Note:** The final three checkmarks mean these outstanding requirements have been identified and disclosed in this report; they do not mean the missing verification or professor confirmation has been completed.

**GitHub repository:**
https://github.com/Rishianandd/NASA-Space-Astronomy-API\
**Backend branch:** `feature/api-backend`\
**Latest pushed commit:** `3ed5653`
