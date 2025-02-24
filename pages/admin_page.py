from pages.base_page import BasePage
import allure


class AdminPage(BasePage):
    """Page object class for Admin Page."""

    def __init__(self, page):
        super().__init__(page)
        self.page_title = page.locator(".title")

    @allure.step("Validating AdminPage Title")
    def get_title(self):
        """Get Title for Admin page.

        Returns:
            string: title of the page
        """
        print(f"title of page : {self.page_title.text_content()}")
        return self.page_title.text_content()
