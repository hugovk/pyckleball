import time
import os
from playwright.sync_api import sync_playwright, Page, expect # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard
from case_variables import *

load_dotenv(find_dotenv(), override=True)


def case_create():
    print("Initiating sample case creation for testing time...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=700)
        page = browser.new_page()
        username = os.getenv("NORMAL_USER_NAME")
        password = os.getenv("NORMAL_USER_PASSWORD")

        login_page = LoginPage(page)
        login_page.login_workflow(username, password)

        dashboard = Dashboard(page)
        page.pause()
        dashboard.deal_with_modal_popups()

        # CREATE A SESSION FOR TESTING PURPOSES
        page.get_by_role("button", name="+ Add Session").click()
        page.locator("#session_location").select_option("1082") # Woburn Raquet Club
        page.click("#session_date")
        page.get_by_role("cell", name="20", exact=True).click()
        page.locator("#session_time").click()
        page.locator("#session_time").select_option("06:00 PM")
        page.locator("#session_time_end").click()
        page.locator("#session_time_end").select_option("06:30 PM")
        page.pause()
        page.locator("#session_waitlist").select_option("0")
        page.locator("#session_title").click()
        page.locator("#session_title").fill("MENS SINGLES MATCH")
        page.locator("#session_release").select_option("1") # option to open the session for sign ups 24 hours in advance
        page.get_by_role("radio", name="No").check()
        page.get_by_role("textbox").nth(2).click()
        page.get_by_role("textbox").nth(2).fill("Singles session.")
        page.get_by_role("checkbox", name="I acknowledge that a play").check()
        try:
            page.get_by_role("button", name="Add Session").click()
        except Exception as e:
            print("There was some error creating a session.")
        print(f"Successfully created a session for day {20} of the current month at 5:00 AM.")

if __name__ == "__main__":
    case_create()
