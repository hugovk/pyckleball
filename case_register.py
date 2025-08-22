from datetime import datetime
# from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from case_common import initialize_case
from print_with_color import print_success, print_blue, print_yellow
from date_variables import case_day, get_url_for_session_starting_on, case_day_for_registering, case_day_my_session_string
from timer import Timer

# CREATE A SESSION FOR TESTING PURPOSES
def case_register():
    print_blue(f"ATTEMPT: Adding registrant to session on {case_day_my_session_string}....")

    with Timer() as timer:
        user_type = "registrant"
        page = initialize_case(user_type)
        page.goto(get_url_for_session_starting_on(case_day))
        # page.pause()
        if user_type == "registrant":
            page.get_by_role("button", name=case_day_for_registering).first.click()
        elif user_type == "pro":
            page.get_by_role("button", name="6:00P : Bedford - John").first.click()
        page.get_by_role("button", name="+ Add My Name").click()
        page.get_by_role("button", name="Close").click()

    print_success(f"SUCCESS: Registrant was added to the session on {case_day_my_session_string}.")

if __name__ == "__main__":
    case_register()
