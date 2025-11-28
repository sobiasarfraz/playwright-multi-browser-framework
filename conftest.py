from symtable import Class

from playwright.sync_api import sync_playwright
from pages.login import Login
from pages.date_picker import DatePickerPage
from pages.tables import TablesPage
from pages.alerts_popups import AlertsPopup
from pages.hover_popupwindows import HoverNewWindow
from logging_helper import setup_logging
import pytest
import os

os.makedirs("videos", exist_ok=True)
# Read the browser name from the environment variable (set by CI)
ci_selected_browser = os.getenv("BROWSER")
browsers_list = [ci_selected_browser] if ci_selected_browser else ["chromium", "firefox", "webkit"]

# -------------- Browser Fixture --------------
#@pytest.fixture(params=["chromium", "firefox", "webkit"],scope="session")
@pytest.fixture(params=browsers_list, scope="session")
def browser(request):
    browser_name = request.param
    with sync_playwright() as p:
        browser_instance = p[browser_name].launch(headless=True, slow_mo=80)


        #####browser = p.chromium.launch(headless=True, slow_mo=50)
        print(f"\n========== Running on: {browser_name.upper()} ==========\n")
        yield browser_instance
        browser_instance.close()

# ---------------- Context Fixture (VIDEO ENABLED) ----------------
@pytest.fixture(scope="session")
def context(browser):

    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        record_video_dir=f"videos/{browser.browser_type.name}/",
        record_video_size={"width": 1920, "height": 1080}
    )

    yield context
    context.close()



# -------------- Page Fixture (Centralized Goto) --------------
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    #page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto("https://testautomationpractice.blogspot.com/")
    yield page
    page.close()


# -------------- Page Object Fixtures (Login, etc.) --------------
@pytest.fixture(scope="session")
def login(page): return Login(page)  # Return an instance of the Login class, passing the `page` object

@pytest.fixture(scope="session")
def dates(page): return DatePickerPage(page)

@pytest.fixture(scope="session")
def tables(page): return TablesPage(page)

@pytest.fixture(scope="session")
def alerts(page): return AlertsPopup(page)

@pytest.fixture(scope="session")
def hover(page): return HoverNewWindow(page)

setup_logging()




