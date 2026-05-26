from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import config


def test_inventory_page_loads_after_login(auth_login):
    inventory = InventoryPage(auth_login.page)
    assert inventory.is_open()
    names = inventory.item_names()
    assert len(names) > 0
    assert "Sauce Labs Backpack" in names


def test_add_item_to_cart(auth_login):
    inventory = InventoryPage(auth_login.page)
    inventory.add_to_cart("Sauce Labs Backpack")

    assert inventory.cart_quantity() == 1
