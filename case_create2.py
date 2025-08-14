from datetime import datetime
from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day_start, case_day_end, case_day_day_one_digit, case_day_start_time_leading_zero, case_day_end_time_leading_zero, get_add_session_start_date, get_one_week_earlier_url_string, get_my_session_string, get_date_one_week_from_today, get_time_string_for_mobley_to_access_session

from case_common import initialize_case
from date_picker_handler import date_picker_handler

# CREATE A SESSION FOR TESTING PURPOSES
def case_create2():
    dashboard = initialize_case("pro")
    page = dashboard
    page.get_by_role("button", name="+ Add Session").click()
    page.locator("#session_location").select_option("1082") # Woburn Racquet Club
    date_picker_handler(page, page.click("#session_date"), case_day_start)
    page.pause()

    page.locator("#session_time").click()
    page.locator("#session_time").select_option(case_day_start_time_leading_zero)
    page.locator("#session_time_end").click()
    page.locator("#session_time_end").select_option(case_day_end_time_leading_zero)
    page.locator("#session_waitlist").select_option("0")
    page.locator("#session_title").click()
    page.locator("#session_title").fill("SINGLES MATCH")
    page.locator("#session_release").select_option("1") # option to open the session for sign ups 24 hours in advance
    page.get_by_role("radio", name="No").check()
    page.get_by_role("textbox").nth(2).click()
    page.get_by_role("textbox").nth(2).fill("Singles session.")
    page.get_by_role("checkbox", name="I acknowledge that a play").check()
    page.pause()
    try:
        page.get_by_role("button", name="Add Session").click()
    except Exception as e:
        print("There was some error creating a session.")
    print(f"Successfully created a session for {get_my_session_string()}.")

if __name__ == "__main__":
    case_create2()
