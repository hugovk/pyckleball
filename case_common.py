from typing import Literal
import os
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv, find_dotenv
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard


def initialize_case(user_type: Literal["pro", "registrant"]) -> Page:
    """
    Initializes the Playwright browser, logs in, and returns a Dashboard object.

    Args:
        username_env (str): The environment variable for the username.
        password_env (str): The environment variable for the password.
        headless (bool): Whether to run the browser in headless mode.
        slow_mo (int): Slow motion delay for debugging.

    Returns:
        a page.
    """

    # load_dotenv(find_dotenv(), override=True)
    # load_dotenv(find_dotenv(), override=False)
    load_dotenv()
    if user_type == "pro":
        username = os.getenv("PRO_USER_NAME")
        password = os.getenv("PRO_USER_PASSWORD")
    elif user_type == "registrant":
        username = os.getenv("REGISTRANT_USER_NAME")
        password = os.getenv("REGISTRANT_USER_PASSWORD")

    print(f"Username = {username}; Password = {password}")

    if not username or not password:
        raise ValueError(f"Environment variables {username} and/or {password} are not set.")

    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Login workflow
    login_page = LoginPage(page)
    login_page.login_workflow(username, password)

    # Initialize the dashboard
    dashboard = Dashboard(page)
    dashboard.deal_with_modal_popups()

    return page


if __name__ == "__main__":
    # Example usage
    dashboard = initialize_case("pro")
    dashboard.pause()
