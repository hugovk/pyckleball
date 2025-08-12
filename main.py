import sys
import time
import os
from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard
from date_variables import *

load_dotenv(find_dotenv(), override=True)
username = os.getenv("PRO_USER_NAME")
password = os.getenv("PRO_USER_PASSWORD")

# username = os.getenv("REGISTRANT_USER_NAME")
# password = os.getenv("REGISTRANT_USER_PASSWORD")

def main():
    print("Hello from pycleball!")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.login_workflow(username, password)

        dashboard = Dashboard(page)
        dashboard.deal_with_modal_popups()

        #THIS IS THE POINT AT WHICH THE REGISTRANT USER AND THE PRO USER DIVERGE
        dashboard.navigate_to_next_weeks_sessions()
        dashboard.select_next_weeks_session()
        page.pause()
        # dashboard.navigate_to_sessions_starting_on(case_day_start) # this takes you to the 21st (it has to be a week earlier)

if __name__ == "__main__":
    main()
