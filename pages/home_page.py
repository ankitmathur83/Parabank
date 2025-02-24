from .base_page import BasePage
import allure


class HomePage(BasePage):
    """Page Object class for HomePage."""
    def __init__(self, page):
        super().__init__(page)
        self.register_link = "text=Register"
        self.about_us_link = page.locator("#headerPanel").get_by_role("link", name="About Us")
        self.services_link = page.locator("#headerPanel").get_by_role("link", name="Services")
        self.products_link = page.locator("#headerPanel").get_by_role("link", name="Products")
        self.locations_link = page.locator("#headerPanel").get_by_role("link", name="Locations")
        self.admin_page_link = page.get_by_role("link", name="Admin Page")
        self.home_page_title = page.locator(".title")
        self.logout_link = page.get_by_role("link", name="Log Out")
        self.user_name_text = page.locator("input[name=\"username\"]")
        self.password_text = page.locator("input[name=\"password\"]")
        self.login_button = page.get_by_role("button", name="Log In")
        self.customer_login_title = page.locator("#leftPanel h2")
        self.customer_welcome_heading = page.locator("#leftPanel b")

    @allure.step("Opening home page")
    def open(self):
        """Open a URL."""
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")

    @allure.step("Navigating to registers link")
    def navigate_to_register(self):
        """Navigate to Register Page."""
        self.page.locator(self.register_link).click()

    @allure.step("Get title of the page")
    def get_title(self):
        """Title for Register Page."""
        title_text = self.home_page_title.text_content()
        return title_text

    @allure.step("Navigate to AboutUs")
    def navigate_to_aboutus(self):
        """Navigate to the AboutUs Page."""

        self.about_us_link.click()

    @allure.step("Navigate to Services")
    def navigate_to_services(self):
        """Navigate to the Services Page."""

        self.services_link.click()

    @allure.step("Navigate to Products")
    def navigate_to_products(self):
        """Navigate to the Products Page."""

        self.products_link.click()

    @allure.step("Navigate to Locations")
    def navigate_to_locations(self):
        """Navigate to the Locations Page."""

        self.locations_link.click()

    @allure.step("Navigate to Admin Page")
    def navigate_to_admin_page(self):
        """Navigate to the Admin Page."""
        
        self.admin_page_link.click()

    def navigate_to(self, page_name: str):
        """Generalise navigation 

        Args:
            page_name (_type_): Page which needs to be navigated.

        Raises:
            ValueError: if page name is not in the dictionary.
        """
        navigation_map = {
            "register": self.navigate_to_register,
            "aboutus": self.navigate_to_aboutus,
            "services": self.navigate_to_services,
            "products": self.navigate_to_products,
            "locations": self.navigate_to_locations,
            "admin_page": self.navigate_to_admin_page,
        }
        if page_name in navigation_map:
            navigation_map[page_name]()
        else:
            raise ValueError(f"Page '{page_name}' does not exist in navigation map.")

    def user_logout(self):
        """logout user 
        """
        self.logout_link.click()
        customer_login_heading = self.customer_login_title.text_content()
        assert "Customer Login" in customer_login_heading

    def user_login(self, user_name: str, password: str):
        """method to login user to the system

        Args:
            user_name (str): username of the user.
            password (str): password of the user.
        """
        self.user_name_text.fill(user_name)
        self.password_text.fill(password)
        self.login_button.click()
        customer_welcome = self.customer_welcome_heading.text_content()
        assert "Welcome" in customer_welcome,f"user is not logged in with error: {customer_welcome}"



