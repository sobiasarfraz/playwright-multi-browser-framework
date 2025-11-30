# Playwright Python Multi-Browser  Automation Framework
[Automation Testing Practice](https://testautomationpractice.blogspot.com/)


Clean Playwright + Python test suite.  
52 stable tests across Chromium, Firefox, and WebKit.  
Full Page Object Model, data-driven flows, and real negative/edge-case coverage.  
Videos, screenshots, and logs committed to main — HTML report available as GitHub Actions artifact.


##  Highlights
- Cross-browser testing (Chromium · Firefox · WebKit)  
- Page Object Model with reusable fixtures  
- Data-driven testing via `@pytest.mark.parametrize`  
- Full-session video recording (one per browser)  
- Selective manual screenshots at critical steps  
- Structured logging (`/Logs` folder)  
- GitHub Actions CI (`.github/workflows/ci.yml`)  
- Self-contained HTML report


## Tech Stack
- Playwright (Python sync API)  
- pytest + pytest-html  
- Python 3.11+

##  Test Coverage
Every major element is tested with **positive + deliberate negative/edge cases**:
- Homepage URL & title verification  
- Full form automation – data-driven (3 valid users) + 6 real negative/edge tests (empty name, invalid email, short phone, special chars, 20→15 char limit, no persistence after refresh)  
- Radio buttons – selection + cannot be unchecked (real behavior)  
- Checkboxes – bulk select + individual uncheck verification  
- Dropdowns – valid selection + option count assertion  
- All 4 date pickers – valid dates + invalid month/day rejection (WebKit-specific handling)  
- Static & dynamic tables – row/column counts, header validation, exact cell lookup, non-existent row checks  
- JavaScript dialogs – alert, confirm (OK/Cancel), prompt (accept/dismiss/empty/bad input) – all flows covered  
- Hover menu – visibility + both sub-links proven broken (negative tests)  
- New Tab button – opens + proves external site is dead (real bug found)  
- Dynamic Start/Stop button – full toggle cycle with proper test isolation (no state leaks)

****Real bugs found and documented through negative testing— not just happy path.****

****52 tests. 100% green across all browsers.****


---

### Project Structure
```plain text
pages/                → Page Objects
tests/                → All test files
videos/               → chromium/, firefox/, webkit/ (full session videos)
screenshots/          → Manual screenshots at key steps
logs/                 → Structured execution logs
.github/              → GitHub Actions workflow
conftest.py           → Browser, page, and video fixtures
screenshot_helper.py  → Screenshot utility
logging_helper.py     → Custom logging setup
README.md
requirements.txt 
```
### How to Run
```plain text
pip install -r requirements.txt
playwright install
```
### All browsers (default)
```
pytest -v --html=reports/report.html --self-contained-html
```

#### Single browser only

| Browser   | Windows PowerShell                                | macOS / Linux / Git Bash                  |
|-----------|----------------------------------------------------|-------------------------------------------|
| Chrome    | `$env:BROWSER="chromium"; pytest -v`              | `BROWSER=chromium pytest -v`              |
| Firefox   | `$env:BROWSER="firefox"; pytest -v`               | `BROWSER=firefox pytest -v`               |
| Safari    | `$env:BROWSER="webkit"; pytest -v`                | `BROWSER=webkit pytest -v`                |

Add `--html=reports/report.html --self-contained-html` to any command when you want the HTML report.
### Output
- reports/report.html – clean HTML report (GitHub Actions artifact)
- Full-session videos in videos/chromium/, videos/firefox/, videos/webkit/
- Manual screenshots at key steps (screenshots/)
- Structured log files (/Log)

All videos, screenshots, and logs are committed to the main branch.
HTML report is available as a GitHub Actions artifact.

All code written and debugged by me.  
No shortcuts. No AI fillers.  
Just clean, working Playwright.

-- Sobia Sarfraz  
November 2025
