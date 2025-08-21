from datetime import datetime
# from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from case_common import initialize_case
from print_with_color import print_success, print_blue, print_yellow
from date_variables import case_day, case_day_start_time, case_day_end_time, get_url_for_session_starting_on, case_day_for_registering, case_day_my_session_string
from timer import Timer

# CREATE A SESSION FOR TESTING PURPOSES
def case_deregister():
    print_blue(f"ATTEMPT: Removing registrant from session on {case_day_my_session_string}....")
    timer = Timer().start()

    page = initialize_case("registrant")
    page.goto(get_url_for_session_starting_on(case_day))
    page.get_by_role("button", name=case_day_for_registering).first.click()
    page.get_by_role("row", name="Mobley Hesperweld (4.0)").get_by_role("img").click()
    page.get_by_role("button", name="Remove").click()

    timer.stop()
    print_success(f"SUCCESS: Registrant was removed from session on {case_day_my_session_string}.")

if __name__ == "__main__":
    case_deregister()
