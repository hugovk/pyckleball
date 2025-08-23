from playwright.sync_api import Page
from playwright.sync_api import expect, TimeoutError  # type: ignore
from datetime import datetime

def date_picker_handler(page: Page, locator, datetime_input: datetime):
    """
    Handles the date picker functionality for selecting a date in the Playtime Scheduler application.
    """
    current_month = datetime.now().strftime("%B")  # Full current_month name
    current_year = datetime.now().strftime("%Y")  # Full current_year

    desired_day = datetime_input.strftime("%-d")  # Day without leading zero
    desired_month = datetime_input.strftime("%B")  # Full desired_month name

    page.get_by_role("cell", name=f"{current_month} {current_year} Toggle Date and").click()
    page.get_by_role("cell", name="Toggle Date and Time Screens").click()
    page.locator("span").filter(has_text=current_year).click()

    page.get_by_text(desired_month[:3], exact=True).click()  # Use first three letters of month
    page.get_by_role("cell", name=desired_day, exact=True).nth(0).click()  # Select the day
