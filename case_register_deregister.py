import time
import os
import sys
from playwright.sync_api import sync_playwright, Page, expect # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard

load_dotenv(find_dotenv(), override=True)

# def case_register_deregister_setup():
#     print("Initiating sample case registration...")

def registration_deregistration_setup():
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
        dashboard.navigate_to_sessions_starting_on("2025-06-14") # this takes you to the 21st (it has to be a week earlier)
        page.get_by_role("button", name="4.0-5.0 6:00A").click()
        # page.pause()

        if not page.locator("role=link[name='Woburn Racquet Club']").is_visible():
            print("Something is wrong, 'Woburn Raquet Club' is not visible - exiting sign up...")
            sys.exit()
        else:
            print("I can see WRC - let's do this!")
        return page

# Sign up Mobley for the session
def register():
    print("Signing Mobley up...")
    page = registration_deregistration_setup()
    page.pause()
    page.get_by_role("button", name="+ Add My Name").click()
    try:
        expect(page.get_by_role("rowgroup")).to_contain_text("2Mobley Hesperweld (4.0)")
        print("SUCCESS: Mobley signed up!")
    except Exception as e:
        print("ERROR: Something happened when Mobley tried to sign up for the session...")

# Delete Mobley from the session
def deregister(page: Page):
    print("Deleting Mobley from the Session...  ")
    # page = registration_deregistration_setup()
    try:
        # page.locator("#viewSessionModal").get_by_text("×").click()
        page.get_by_role("row", name="Mobley Hesperweld (4.0)").get_by_role("img").click()
        page.get_by_role("button", name="Remove").click()
        print("SUCCESS: Mobley successfully removed from session.")
    except Exception as e:
        print("ERROR: Something happened when trying to remove Mobley from the session...")

if __name__ == "__main__":
    register()
