from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day_my_session_string

from case_common import initialize_case

from page_objects.dashboard import Dashboard

def case_delete():
    print(f"ATTEMPT: Case_delete.py is deleting pro session for {case_day_my_session_string}.")
    page = initialize_case("pro")
    page.get_by_role("button", name="My Sessions").click()
    page.get_by_role("link", name=case_day_my_session_string).click()
    page.get_by_role("link", name="Edit/Cancel Session...").click()
    page.get_by_role("button", name="CANCEL SESSION").click()
    page.pause()
    page.get_by_role("button", name="Cancel Session", exact=True).click()
    print(f"SUCCESS: Case_delete.py deleted session for {case_day_my_session_string}.")

if __name__ == "__main__":
    case_delete()
