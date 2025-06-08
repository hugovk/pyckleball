import sys
import time
import os
from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard
from date_variables import get_my_session_string

load_dotenv(find_dotenv(), override=True)

def case_delete():
    print("Initiating test case deletion...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        username = os.getenv("NORMAL_USER_NAME")
        password = os.getenv("NORMAL_USER_PASSWORD")

        login_page = LoginPage(page)
        login_page.login_workflow(username, password)

        dashboard = Dashboard(page)
        dashboard.deal_with_modal_popups()

        #insert code here to delete a session.
        dashboard.click_my_sessions()

        session_string_to_find = get_my_session_string()
        try:
            page.get_by_role("link", name=session_string_to_find).click(timeout=3000)
        except TimeoutError:
            print(f"No session found for '{session_string_to_find}'. Exiting case_delete.py")
            sys.exit()

        page.get_by_role("link", name="Edit/Cancel Session...").click()
        page.get_by_role("button", name="CANCEL SESSION").click()
        page.get_by_role("button", name="Cancel Session", exact=True).click()
        print("Test case session deleted.")


if __name__ == "__main__":
    case_delete()
