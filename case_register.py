import time
import os
import sys
from playwright.sync_api import sync_playwright, Page, expect # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard
from date_variables import *

load_dotenv(find_dotenv(), override=True)

def case_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        username = os.getenv("ALTERNATIVE_USER_NAME")
        password = os.getenv("ALTERNATIVE_USER_PASSWORD")

        login_page = LoginPage(page)
        login_page.login_workflow(username, password)

        dashboard = Dashboard(page)
        dashboard.deal_with_modal_popups()

        # Find the session to sign up for.
        dashboard.navigate_to_sessions_starting_on(case_day_start) # this takes you to the 21st (it has to be a week earlier)
        session_string_to_click = "4.0-5.0 " + get_time_string_for_mobley_to_access_session()
        page.get_by_role("button", name=session_string_to_click).click()
        # page.pause()

        if not page.locator("role=link[name='Woburn Racquet Club']").is_visible():
            print("Something is wrong, 'Woburn Raquet Club' is not visible - exiting sign up...")
            sys.exit()
        else:
            print("I can see WRC - let's do this!")

        print("Signing Mobley up...")
        # page.pause()
        page.get_by_role("button", name="+ Add My Name").click()
        try:
            expect(page.get_by_role("rowgroup")).to_contain_text("2Mobley Hesperweld (4.0)")
            print("SUCCESS: Mobley signed up!")
        except Exception as e:
            print("ERROR: Something happened when Mobley tried to sign up for the session...")

        # # Delete Mobley from the session
        # print("Deleting Mobley from the Session...  ")
        # try:
        #     page.get_by_role("row", name="Mobley Hesperweld (4.0)").get_by_role("img").click()
        #     page.get_by_role("button", name="Remove").click()
        #     print("SUCCESS: Mobley successfully removed from session.")
        # except Exception as e:
        #     print("ERROR: Something happened when trying to remove Mobley from the session...")

if __name__ == "__main__":
    case_register()
