from playwright import sync_api

from pages.base_page import BasePage
import allure

class Locations(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.locator(".page-title")

    @allure.step("Validating Locations Title")
    def get_title(self):
        print(f"title of page : {self.page_title.text_content()}")
        return self.page_title.text_content()