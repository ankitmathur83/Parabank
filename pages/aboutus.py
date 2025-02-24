import allure
from pages.base_page import BasePage


class AboutUs(BasePage):
    """Page object class for AboutUs page

    Args:
        BasePage (_type_): Calling BasePage class for the creating page and further use.
    """
    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.locator(".title")

    @allure.step("validate About us title")
    def get_title(self):
        """Get Title of About us page"""
        print(f"title of page : {self.page_title.text_content()}")
        return self.page_title.text_content()
