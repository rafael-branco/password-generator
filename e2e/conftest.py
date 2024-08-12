# conftest.py
import sys
import os
import pytest
from playwright.sync_api import sync_playwright

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
    page = context.new_page()
    yield page
    page.close()
    context.close()
