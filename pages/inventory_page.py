from .base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_container = self.page.locator(".inventory_list")
        self.product_label = self.page.locator(".inventory_item_name")
        self.cart_badge = self.page.locator(".shopping_cart_badge")
        self.cart_link = self.page.locator(".shopping_cart_link")

    def is_open(self) -> bool:
        return self.inventory_container.is_visible()

    def item_names(self) -> list[str]:
        return [text.strip() for text in self.product_label.all_text_contents()]

    def add_to_cart(self, item_name: str):
        item_locator = self.page.locator(
            ".inventory_item",
            has=self.page.get_by_text(item_name, exact=True),
        )
        item_locator.get_by_role("button", name="Add to cart").click()

    def cart_quantity(self) -> int:
        if self.cart_badge.is_visible():
            return int(self.cart_badge.text_content().strip())
        return 0

    def open_cart(self):
        self.cart_link.click()
