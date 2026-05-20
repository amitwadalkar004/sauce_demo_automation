import pytest

from pages.login_page import LoginPage
from utils.config import config

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
    return login_page
