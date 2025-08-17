from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day, case_day_my_session_string, case_day_start_time, case_day_end_time

from case_common import initialize_case
from date_picker_handler import date_picker_handler

# CREATE A SESSION FOR TESTING PURPOSES
def case_create():
    print(f"ATTEMPT: Case_create.py is creating pro session for {case_day_my_session_string}.")
    dashboard = initialize_case("pro")
    page = dashboard
    page.get_by_role("button", name="+ Add Session").click()

    page.locator("#session_location").select_option("1082") # Woburn Racquet Club
    date_picker_handler(page, page.click("#session_date"), case_day)
    page.locator("#session_time").click()
    page.locator("#session_time").select_option(case_day_start_time)
    page.locator("#session_time_end").click()
    page.locator("#session_time_end").select_option(case_day_end_time)
    page.locator("#session_waitlist").select_option("0")
    page.locator("#session_title").click()
    page.locator("#session_title").fill("SINGLES MATCH")
    # page.pause()
    page.locator("#session_release").select_option("0") # option to open the session for sign ups immediately
    # page.locator("#session_release").select_option("1") # option to open the session for sign ups 24 hours in advance
    page.get_by_role("radio", name="No").check()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("Singles session.")
    page.get_by_role("checkbox", name="I acknowledge that a play").check()
    page.pause()
    page.get_by_role("button", name="Add Session").click()
    print(f"SUCCESS: Case_create.py created session for {case_day_my_session_string}.")

if __name__ == "__main__":
    case_create()
