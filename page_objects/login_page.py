import os
from dotenv import load_dotenv, find_dotenv
from playwright.sync_api import Page, Locator
# load_dotenv(find_dotenv(), override=True)

class LoginPage:
    # def __init__(self, page, username: str = None, password: str = None) -> None:
    #     self.page = page
    #     self.page.goto(os.getenv("HOST_URL"))
    #     self.username = username
    #     self.password = password

    # def populate_email(self):
    #     self.page.locator('input[name="email"]').fill(self.username)

    # def click_login_after_entering_email(self):
    #     self.page.get_by_role("button", name="Login").click()

    # def populate_password(self):
    #     self.page.locator("#password").fill(self.password)

    # def click_login_after_entering_password(self):
    #     self.page.get_by_role("button", name="Login").click()

    # def login_workflow(self):
    #     self.populate_email()
    #     self.click_login_after_entering_email()
    #     self.populate_password()
    #     self.click_login_after_entering_password()

    def __init__(self, page) -> None:
        self.page = page
        self.page.goto("https://playtimescheduler.com/login.php")

    # def test_function(self) -> None:
    #     print("This is a test function in the LoginPage class.")

    def populate_email(self, email: str) -> None:
        self.page.locator('input[name="email"]').fill(email)

    def click_login_after_entering_email(self) -> None:
        self.page.get_by_role("button", name="Login").click()

    def populate_password(self, password: str) -> None:
        self.page.locator("#password").fill(password)

    def click_login_after_entering_password(self):
        self.page.get_by_role("button", name="Login").click()

    def login_workflow(self, username: str, password: str) -> None:
        self.populate_email(username)
        self.click_login_after_entering_email()
        self.populate_password(password)
        self.click_login_after_entering_password()
