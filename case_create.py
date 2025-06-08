import time
import os
from playwright.sync_api import sync_playwright, Page, expect # type: ignore

from dotenv import load_dotenv, find_dotenv # type: ignore
from page_objects.login_page import LoginPage
from page_objects.dashboard import Dashboard
from date_variables import *

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
        dashboard.deal_with_modal_popups()

        # CREATE A SESSION FOR TESTING PURPOSES
        page.get_by_role("button", name="+ Add Session").click()
        page.locator("#session_location").select_option("1082") # Woburn Racquet Club
        page.click("#session_date")
        page.get_by_role("cell", name=case_day_day_one_digit, exact=True).click()
        page.locator("#session_time").click()
        page.locator("#session_time").select_option(case_day_start_time_leading_zero)
        page.locator("#session_time_end").click()
        page.locator("#session_time_end").select_option(case_day_end_time_leading_zero)
        page.pause()
        page.locator("#session_waitlist").select_option("0")
        page.locator("#session_title").click()
        page.locator("#session_title").fill("SINGLES MATCH")
        page.locator("#session_release").select_option("1") # option to open the session for sign ups 24 hours in advance
        page.get_by_role("radio", name="No").check()
        page.get_by_role("textbox").nth(2).click()
        page.get_by_role("textbox").nth(2).fill("Singles session.")
        page.get_by_role("checkbox", name="I acknowledge that a play").check()
        try:
            page.get_by_role("button", name="Add Session").click()
        except Exception as e:
            print("There was some error creating a session.")
        print(f"Successfully created a session for {get_my_session_string()}.")

if __name__ == "__main__":
    case_create()
