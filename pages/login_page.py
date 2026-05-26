from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = self.page.get_by_placeholder("Username")
        self.password = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.menu_button = self.page.get_by_role("button", name="Open Menu")
        self.logout_link = self.page.get_by_role("link", name="Logout")
        self.error_message = self.page.locator("h3[data-test='error']")

    def navigate(self, url: str):
        self.goto(url)

    def login(self, username: str, password: str):
        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_button)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)

    def get_error(self) -> str:
        return self.text_content(self.error_message)
