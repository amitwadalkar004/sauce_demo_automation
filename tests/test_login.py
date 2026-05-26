from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import config


def test_successful_login(auth_login):
    inventory = InventoryPage(auth_login.page)
    assert inventory.is_open()


def test_invalid_login_shows_error(page, base_url):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login("bad_user", "bad_password")
    assert "Epic sadface" in login.get_error()
