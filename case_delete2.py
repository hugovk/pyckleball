from playwright.sync_api import sync_playwright, Page, expect, TimeoutError # type: ignore

from date_variables import case_day_my_session_string

from case_common import initialize_case

from page_objects.dashboard import Dashboard

def case_delete2():
    print(f"Deleting pro session for {case_day_my_session_string}.")
    page = initialize_case("pro")
    # dashboard = Dashboard(page)
    # dashboard.click_my_sessions()
    page.get_by_role("button", name="My Sessions").click()
    page.get_by_role("link", name=case_day_my_session_string).click()
    page.get_by_role("link", name="Edit/Cancel Session...").click()
    page.get_by_role("button", name="CANCEL SESSION").click()
    page.pause()
    page.get_by_role("button", name="Cancel Session", exact=True).click()
    print(f"Success: Test case session for '{case_day_my_session_string}' has been deleted.")

if __name__ == "__main__":
    case_delete2()
