import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.page.goto(os.getenv("HOST_URL"))

    def populate_email(self, email):
        self.page.locator('input[name="email"]').fill(email)

    def click_login_after_entering_email(self):
        self.page.get_by_role("button", name="Login").click()

    def populate_password(self, password):
        self.page.locator("#password").fill(password)

    def click_login_after_entering_password(self):
        self.page.get_by_role("button", name="Login").click()

    def login_workflow(self, email, password):
        self.populate_email(email)
        self.click_login_after_entering_email()
        self.populate_password(password)
        self.click_login_after_entering_password()
