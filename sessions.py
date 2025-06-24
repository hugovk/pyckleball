from dataclasses import dataclass
import os
from playwright.sync_api import Page

from dotenv import load_dotenv, find_dotenv
from page_objects.login_page import LoginPage


class Session:
    # timeout: int = 30000
    # host_url: str = "https://playtimescheduler.com/login.php"
    # username: str | None = None
    # password: str | None = None

    def __post_init__(self, page: Page) -> None:
        # self.password = os.getenv("USER_PASSWORD")
        # self.timeout = int(os.getenv("TIMEOUT_IN_MS"))
        self.login_page = LoginPage(page)

    # def login(self, page: Page) -> None:
    #     load_dotenv(find_dotenv(), override=True)
    #     page.goto(self.host_url)
    #     print(f"Logging in as {self.username}...")
    #     page.fill("input[id='email']", self.username)
    #     page.fill("input[id='password']", self.password)

    #     # Click the login button.
    #     page.click("button[type='submit']")


class ProSession(Session):
    def __post_init__(self):
        super().__post_init__()
        self.username = os.getenv("PRO_USER_EMAIL")
        self.password = os.getenv("PRO_USER_PASSWORD")

class RegistrantSession(Session):
    def __post_init__(self):
        super().__post_init__()
        self.username = os.getenv("REGISTRANT_USER_EMAIL")
        self.password = os.getenv("REGISTRANT_USER_PASSWORD")


if __name__ == "__main__":
    my_test_session = RegistrantSession()
    print(my_test_session.username)
    print(my_test_session.password)
