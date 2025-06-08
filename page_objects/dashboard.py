import sys
import time
from playwright.sync_api import sync_playwright, Page, TimeoutError, expect  # type: ignore
from date_variables import *

class Dashboard():
    def __init__(self, page: Page):
        self.page = page

    def exit_modal_of_ad_if_applicable(self):

        try:
            close_button1 = self.page.get_by_role("button", name="CLOSE", exact=True)
            close_button1.click()
            print("Successfully closed the ad modal...")
        except TimeoutError:
            print("The ad modal did not appear or was not interactable - exiting function to address it...")
        except Exception as e:
            print(f"An unexpected error occurred with the ad modal: {e}")

    def exit_modal_of_code_of_conduct_if_applicable(self):

        try:
            got_it_button = self.page.get_by_role("button", name="Got It!", exact=True)
            got_it_button.click(timeout=2000)  # Set timeout to 3000ms
            print("Successfully closed the 'Code of Conduct' modal...")
        except TimeoutError:
            print("The 'Code of Conduct' modal did not appear or was not interactable within 3 seconds, moving on...")
        except Exception as e:
            print(f"An unexpected error occurred with the 'Code of Conduct' modal: {e}")

    def deal_with_modal_popups(self):
        self.exit_modal_of_ad_if_applicable()
        self.exit_modal_of_code_of_conduct_if_applicable()

    def navigate_to_sessions_starting_on(self, datetime_input):
        url_base = "https://playtimescheduler.com/index.php?go=next&startDate="
        url_for_next_weeks_session = url_base + get_one_week_earlier_url_string(datetime_input)
        self.page.goto(url_for_next_weeks_session)

    def navigate_to_next_weeks_sessions(self):
        """
        It's possible to access a specific date range by clicking on the calendar button and then selecting the date, but this is more problematic programmatically. Instead, we can simply enter in the URL for the range in question, which appears in the form:
        `https://playtimescheduler.com/index.php?go=next&startDate=2025-06-04`
        Where the date at the end of the string is the date 1 week before the date we want to access. So, the URL shown above would show the week starting on June 11, 2025 and ending a week later on June 18, 2025.
        """
        url_base = "https://playtimescheduler.com/index.php?go=next&startDate="
        url_for_next_weeks_session = url_base + get_date_one_week_from_today()
        self.page.goto(url_for_next_weeks_session)

    def select_next_weeks_session(self):
        # Check if the link is visible
        if self.page.get_by_role("link", name="Welcome, Mobley Hesperweld!").is_visible():
            expect(self.page.get_by_role("link", name="Welcome, Mobley Hesperweld!")).to_be_visible()
            self.page.get_by_role("button", name="4.0-5.0 6:30P ").click()
        else:
            self.page.get_by_role("button", name=" 6:30P : Bedford - John Glenn Middle School – 4.0-").click()

    def click_add_session(self):
        self.page.get_by_role("button", name="+ Add Session").click()

    def click_my_sessions(self):
        self.page.get_by_role("button", name="My Sessions").click()
