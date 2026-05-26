from playwright.sync_api import Locator, Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def locator(self, selector: str | Locator):
        if isinstance(selector, Locator):
            return selector
        return self.page.locator(selector)

    def fill(self, selector: str | Locator, value: str):
        self.locator(selector).fill(value)

    def click(self, selector: str | Locator):
        self.locator(selector).click()

    def text_content(self, selector: str | Locator) -> str:
        return self.locator(selector).text_content() or ""

    def is_visible(self, selector: str | Locator) -> bool:
        return self.locator(selector).is_visible()
