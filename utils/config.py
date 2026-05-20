from dataclasses import dataclass

@dataclass
class SauceDemoConfig:
    base_url: str = "https://www.saucedemo.com/"
    username: str = "standard_user"
    password: str = "secret_sauce"

config = SauceDemoConfig()
