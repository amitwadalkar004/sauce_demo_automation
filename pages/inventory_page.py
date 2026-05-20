from .base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = ".inventory_list"
    PRODUCT_LABEL = ".inventory_item_name"

    def is_open(self) -> bool:
        return self.is_visible(self.INVENTORY_CONTAINER)

    def item_names(self) -> list[str]:
        return [element.text_content().strip() for element in self.page.query_selector_all(self.PRODUCT_LABEL)]
