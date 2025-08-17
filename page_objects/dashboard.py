from playwright.sync_api import sync_playwright, Page, TimeoutError, expect  # type: ignore
from date_variables import *

class Dashboard():
    def __init__(self, page: Page):
        self.page = page

    def exit_modal_of_ad_if_applicable(self):

        try:
            close_button1 = self.page.get_by_role("button", name="CLOSE", exact=True)
            close_button1.click()
            # print("Successfully closed the ad modal...")
        except TimeoutError:
            print("The ad modal did not appear or was not interactable - exiting function to address it...")
        except Exception as e:
            print(f"An unexpected error occurred with the ad modal: {e}")

    def deal_with_modal_popups(self):
        self.exit_modal_of_ad_if_applicable()
