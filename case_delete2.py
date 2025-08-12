from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day_start, case_day_end, case_day_day_one_digit, case_day_start_time_leading_zero, case_day_end_time_leading_zero, get_add_session_start_date, get_one_week_earlier_url_string, get_my_session_string, get_date_one_week_from_today, get_time_string_for_mobley_to_access_session

from case_common import initialize_case

from page_objects.dashboard import Dashboard

import sys

def case_delete2():
    page = initialize_case("pro")
    dashboard = Dashboard(page)
    dashboard.click_my_sessions()
    session_string_to_find = get_my_session_string()
    print(session_string_to_find)
    page.pause()

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
    case_delete2()
