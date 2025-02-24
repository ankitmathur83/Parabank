import allure
from pages.base_page import BasePage


class Products(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.locator(".page-title")

    @allure.step("validate Products title")
    def get_title(self):
        print(f"title of page : {self.page_title.text_content()}")
        return self.page_title.text_content()