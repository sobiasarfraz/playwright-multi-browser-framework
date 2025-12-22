# Playwright Python Multi-Browser  Automation Framework
[Automation Testing Practice](https://testautomationpractice.blogspot.com/)


Clean Playwright + Python test suite.  
52 stable tests across Chromium, Firefox, and WebKit using a full Page Object Model, reusable fixtures/helpers, data-driven flows with deliberate real negative/edge-case coverage.
Integrated with Docker, GitHub Actions CI, and AWS (S3, CloudWatch, IAM/OIDC) for realistic, production-style execution.


##  Highlights
- Cross-browser testing (Chromium · Firefox · WebKit)  
- Page Object Model with reusable fixtures  
- Data-driven testing via `@pytest.mark.parametrize`  
- GitHub Actions CI with Dockerized execution
- Full-session video recording (one per browser)  
- Selective manual screenshots at critical steps
- Structured logging committed locally for visibility, streamed to AWS CloudWatch for EC2 executions
- HTML reports uploaded as GitHub Actions artifacts and to AWS S3 (CI + cloud runs)
- AWS integration (S3 reports, CloudWatch logs, secure IAM/OIDC authentication)

## Tech Stack
- Playwright (Python sync API)  
- pytest + pytest-html  
- Python 3.11+
- Docker (containerized execution)
- GitHub Actions (CI pipeline)
- AWS (S3, CloudWatch, EC2, IAM/OIDC)

##  Test Coverage
Every UI area is tested with **positive + deliberate negative/edge cases**:

- Homepage: URL and title verification
- Forms: data-driven valid submissions + 6 negative cases (empty name, invalid email, short phone, special characters, length validation, refresh persistence)
- Inputs: radio buttons, checkboxes, dropdowns, all 4 date pickers
- Data: static and dynamic tables (row/column counts, header validation, exact cell lookup, non-existent rows)
- Behavior: JavaScript dialogs (alert, confirm, prompt), hover menu with broken links confirmed, new tab to dead external site, dynamic Start/Stop toggle with proper state isolation

Real bugs confirmed through negative testing — not just happy-path validation.
52 tests — passing across Chromium, Firefox, and WebKit.




### Project Structure
```text
pages/                → Page Objects
tests/                → All test files
videos/               → chromium/, firefox/, webkit/ (full session videos)
screenshot/          → Manual screenshots at key steps
Logs/                 → Structured execution logs
.github/              → GitHub Actions workflow
conftest.py           → Browser, page, and video fixtures
Dockerfile            → Containerized execution
screenshot_helper.py  → Screenshot utility
logging_helper.py     → Custom logging setup
README.md
requirements.txt 
```

## Running Tests Locally (Without Docker)

#### Install dependencies
```text
pip install -r requirements.txt
playwright install
```
#### Run all browsers
```
pytest -v -s
```

#### Single browser only

| Browser   | Windows PowerShell                      | macOS / Linux / Git Bash        |
|-----------|-----------------------------------------|---------------------------------|
| Chrome    | `$env:BROWSER="chromium"; pytest -v -s` | `BROWSER=chromium pytest -v -s` |
| Firefox   | `$env:BROWSER="firefox"; pytest -v -s`  | `BROWSER=firefox pytest -v -s`  |
| Safari    | `$env:BROWSER="webkit"; pytest -v -s`   | `BROWSER=webkit pytest -v -s`   |

Add `--html=reports/report.html --self-contained-html` to any command when you want the HTML report.

## Running Tests Using Docker (Recommended)

#### build Docker image 
```
docker build -t playwright-project .
```
#### Run Tests (default configuration)
```
docker run --rm -it playwright-project
```
#### Run Tests and capture reports, videos, screenshots, and logs locally
```
docker run --rm \
  -v "$(pwd)/videos:/playwright/videos" \
  -v "$(pwd)/screenshot:/playwright/screenshot" \
  -v "$(pwd)/Logs:/playwright/Logs" \
  -v "$(pwd)/reports:/playwright/reports" \
  playwright-project
  ```
This mounts your local folders so videos, screenshots and logs are saved.

### Output

- HTML report uploaded to AWS S3 (permanent) and GitHub Actions artifacts (temporary)
- Structured execution logs committed to the repository and streamed to **AWS CloudWatch** for EC2 runs
- Full-session browser videos and screenshots captured per execution (committed for portfolio visibility)

All code written and debugged by me.
— Sobia Sarfraz  
December 2025
