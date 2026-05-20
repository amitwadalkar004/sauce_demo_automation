from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import config


def test_inventory_page_loads_after_login(page, base_url):
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(config.username, config.password)

    inventory = InventoryPage(page)
    assert inventory.is_open()
    names = inventory.item_names()
    assert len(names) > 0
    assert "Sauce Labs Backpack" in names
