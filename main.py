import time
import os
from playwright.sync_api import sync_playwright, Page, expect # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard

load_dotenv(find_dotenv(), override=True)

def main():
    print("Hello from pycleball!")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        username = os.getenv("ALTERNATIVE_USER_NAME")
        password = os.getenv("ALTERNATIVE_USER_PASSWORD")

        login_page = LoginPage(page)
        login_page.login_workflow(username, password)

        dashboard = Dashboard(page)
        dashboard.deal_with_modal_popups()
        dashboard.navigate_to_next_weeks_sessions()
        dashboard.select_next_weeks_session()
        page.pause()
        dashboard.navigate_to_specific_days_sessions("2025-06-14") # this takes you to the 21st (it has to be a week earlier)

if __name__ == "__main__":
    main()
