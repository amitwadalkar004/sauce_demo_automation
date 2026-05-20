from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    def click(self, selector: str):
        self.page.click(selector)

    def text_content(self, selector: str) -> str:
        return self.page.text_content(selector) or ""

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
