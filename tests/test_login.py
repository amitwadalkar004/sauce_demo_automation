from pages.login_page import LoginPage
from utils.config import config


def test_successful_login(page, base_url):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(config.username, config.password)
    assert page.locator(".inventory_list").is_visible()


def test_invalid_login_shows_error(page, base_url):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("bad_user", "bad_password")
    assert "Epic sadface" in login.get_error()
