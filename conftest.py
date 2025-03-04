from datetime import datetime
import pytest
import configparser
from playwright.sync_api import sync_playwright



@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser(request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def setup_page(browser):
    context = browser.new_context()
    api_request_context = context.request
    page = context.new_page()
    yield page, api_request_context
    context.close()


@pytest.fixture(scope="session")
def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

@pytest.fixture(scope="function",autouse=True)
def take_screenshots_always(setup_page):
    page, api_request_context = setup_page  # Extract the page from the setup_page fixture
    yield
    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/screenshot_{timestamp}.png"

    # Take screenshot of the page, not the browser
    page.screenshot(path=screenshot_path, full_page=True)


