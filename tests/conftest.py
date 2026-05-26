import os
from datetime import datetime
from pathlib import Path

import pytest

from pages.login_page import LoginPage
from utils.config import config

REPORTS_DIR = Path(__file__).resolve().parents[1] / "reports"
SCREENSHOT_DIR = REPORTS_DIR / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

@pytest.fixture(scope="session")
def base_url() -> str:
    return config.base_url

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def auth_login(login_page, base_url):
    login_page.navigate(base_url)
    login_page.login(config.username, config.password)

    login_page.page.locator(".inventory_list").wait_for(state="visible")
    screenshot_path = SCREENSHOT_DIR / f"login_success_{datetime.now():%Y%m%d_%H%M%S}.png"
    login_page.page.screenshot(path=str(screenshot_path), full_page=True)

    yield login_page

    try:
        login_page.logout()
    except Exception:
        pass
