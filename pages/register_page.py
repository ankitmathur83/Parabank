import time

import allure, string, random
from playwright.sync_api import Page

from pages.base_page import BasePage


class RegisterPage(BasePage):
    USER_PASSWORD = "fabric@123"  #Hardcoded to keep the password same for all the accounts created randomly. #Easy to diagnose

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://parabank.parasoft.com/parabank/register.htm"
        self.first_name_text = page.locator("[id=\"customer\\.firstName\"]")
        self.last_name_text = page.locator("[id=\"customer\\.lastName\"]")
        self.street_text = page.locator("[id=\"customer\\.address\\.street\"]")
        self.city_text = page.locator("[id=\"customer\\.address\\.city\"]")
        self.state_text = page.locator("[id=\"customer\\.address\\.state\"]")
        self.zip_code_text = page.locator("[id=\"customer\\.address\\.zipCode\"]")
        self.phone_number_text = page.locator("[id=\"customer\\.phoneNumber\"]")
        self.ssn_text = page.locator("[id=\"customer\\.ssn\"]")
        self.username_text = page.locator("[id=\"customer\\.username\"]")
        self.password_text = page.locator("[id=\"customer\\.password\"]")
        self.confirm_password_text = page.locator("[id=repeatedPassword]")
        self.register_button = page.get_by_role("button", name="Register")


    @allure.step("Register New User")
    def register_user(self, first_name=None, last_name=None, street_name=None, city_name=None, state_name=None,
                      zip_code=None, phone_number=None,
                      ssn_number=None, confirm_password=None):
        self.first_name_text.fill(first_name)
        self.last_name_text.fill(last_name)
        self.street_text.fill(street_name)
        self.city_text.fill(city_name)
        self.state_text.fill(state_name)
        self.zip_code_text.fill(zip_code)
        self.phone_number_text.fill(phone_number)
        self.ssn_text.fill(ssn_number)
        self.user_name = self._generate_username()
        self.username_text.fill(self.user_name)
        self.password_text.fill(RegisterPage.USER_PASSWORD)
        self.confirm_password_text.fill(RegisterPage.USER_PASSWORD)
        time.sleep(2)
        self.register_button.click()

    @allure.step("Check if register page is loaded")
    def get_tile(self):
        title_text = self.register_page_title.text_content()
        return title_text

    def _generate_username(self):
        "Method to generate Username randomly."
        characters = string.ascii_letters
        for _ in range(5):
            return ''.join(random.choice(characters) for _ in range(5))


if __name__ == "__main__":
    reg = RegisterPage()
    reg.generate_username()
