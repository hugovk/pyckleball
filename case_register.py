from datetime import datetime
from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day, get_url_for_session_starting_on, case_day_for_registering, case_day_my_session_string

from case_common import initialize_case
from date_picker_handler import date_picker_handler

# CREATE A SESSION FOR TESTING PURPOSES
def case_register():
    print(f"ATTEMPT: Case_register.py is adding the registrant to the session on {case_day_my_session_string}....")

    page = initialize_case("registrant")
    page.goto(get_url_for_session_starting_on(case_day))
    page.get_by_role("button", name=case_day_for_registering).click()
    page.get_by_role("button", name="+ Add My Name").click()
    page.get_by_role("button", name="Close").click()
    print(f"SUCCESS: Case_register.py added the registrant to the session on {case_day_my_session_string}.")

if __name__ == "__main__":
    case_register()
