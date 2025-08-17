from datetime import datetime
from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day, case_day_start_time, case_day_end_time, get_url_for_session_starting_on, case_day_for_registering, case_day_my_session_string

from case_common import initialize_case
from date_picker_handler import date_picker_handler

# CREATE A SESSION FOR TESTING PURPOSES
def case_deregister():
    page = initialize_case("registrant")
    page.goto(get_url_for_session_starting_on(case_day))
    page.get_by_role("button", name=case_day_for_registering).click()
    page.get_by_role("row", name="Mobley Hesperweld (4.0)").get_by_role("img").click()
    page.get_by_role("button", name="Remove").click()
    print(f"SUCCESS: Mobley was removed from session on {case_day}.")

if __name__ == "__main__":
    case_deregister()
