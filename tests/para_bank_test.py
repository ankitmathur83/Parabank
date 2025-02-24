import time

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.aboutus import AboutUs
from pages.services import Services
from pages.products import Products
from pages.locations import Locations
from pages.admin_page import AdminPage
from api.transaction import Transaction_API

from utils.logger import setup_logger

logger = setup_logger()


def test_account_service_flow(setup_page, load_config):
    home_page = HomePage(setup_page[0])
    register_page = RegisterPage(setup_page[0])
    services_page = Services(setup_page[0])
    transaction_api = Transaction_API(setup_page[0])

    # reading parameters from config.ini file
    config = load_config
    first_name = config["user_info"]["first_name"]
    last_name = config["user_info"]["last_name"]
    address = config["user_info"]["address"]
    city = config["user_info"]["city"]
    state = config["user_info"]["state"]
    zip_code = config["user_info"]["zip_code"]
    phone_number = config["user_info"]["phone_number"]
    ssn = config["user_info"]["ssn"]

    logger.info("Test: test_account_service_flow started")

    logger.info("Opening the Home Page")
    home_page.open()

    logger.info("Navigating to register page")
    home_page.navigate_to_register()
    assert "Signing up is easy!" in home_page.get_title(), "Register page is not displayed"
    logger.info("Successfully Navigated to Register Page")

    logger.info("Registering a User")
    register_page.register_user(first_name, last_name, address, city, state, zip_code, phone_number, ssn)
    assert ("Welcome " + register_page.user_name in home_page.get_title())
    logger.info("Successfully registered a User and auto-Logged In")

    logger.info("Logging out user")
    home_page.user_logout()

    logger.info("Logging back user again")
    home_page.user_login(register_page.user_name, "fabric@123")

    account_id = services_page.open_savings_account("SAVINGS")
    assert "Account Opened!" in services_page.open_account_status()
    logger.info("Successfully opened a Savings Account")
    logger.info(f"Account ID is: {account_id}")

    logger.info("Verifying Account Balance")
    account_balance = services_page.account_overview(account_id)
    logger.info(f"Account Balance is: {account_balance}")

    # Hardcoding $100 this value as system creates account with this amount.
    assert "$100" in account_balance, "Mismatch in Account Balance"

    logger.info("Transferring Funds from newly created account.")
    amount_to_transfer = "10"
    transfer_complete_text = services_page.transfer_funds_from_account(account_id, amount_to_transfer)
    assert "Transfer Complete!" in transfer_complete_text, "Failed to transfer funds"
    api_response = transaction_api.get_account_transactions_by_amount(account_id, amount_to_transfer)
    assert "Funds Transfer Sent" in [(item['description']) for item in api_response]
    logger.info("Transferring is completed successfully")

    logger.info("Paying the bill with newly created account")

    # read config file
    payee_name = config["bill_payee"]["payee_name"]
    payee_address = config["bill_payee"]["address"]
    payee_city = config["bill_payee"]["city"]
    payee_state = config["bill_payee"]["state"]
    payee_zip_code = config["bill_payee"]["zip_code"]
    payee_phone_number = config["bill_payee"]["phone_number"]
    payee_account_number = config["bill_payee"]["account_number"]
    payee_amount = config["bill_payee"]["amount"]

    bill_pay_status = services_page.pay_bill(payee_name, payee_address, payee_city,
                                             payee_state, payee_zip_code, payee_phone_number,
                                             payee_account_number, payee_amount, account_id)

    assert "Bill Payment Complete" in bill_pay_status
    logger.info("Bill Payment is successful.")
    time.sleep(3)
    logger.info("Checking account transaction by amount using API")
    api_response = transaction_api.get_account_transactions_by_amount(account_id, amount_to_transfer)
    assert "Bill Payment to engaus" in [(item['description']) for item in api_response]


def test_global_navigation(setup_page):
    home_page = HomePage(setup_page[0])
    about_page = AboutUs(setup_page[0])
    services_page = Services(setup_page[0])
    products_page = Products(setup_page[0])
    location_page = Locations(setup_page[0])
    admin_page = AdminPage(setup_page[0])

    home_page.open()
    logger.info("Navigate to About Us Page")
    home_page.navigate_to("aboutus")
    assert ("ParaSoft Demo Website" in about_page.get_title())
    logger.info("Navigating to About Us Page is Successful")

    logger.info("Navigate to Services Page")
    home_page.navigate_to("services")
    assert ("CXF - Service list" in services_page.get_title())
    logger.info("Navigating to Services Page is Successful")

    logger.info("Navigate to Products Page")
    home_page.navigate_to("products")
    assert ("Products" in products_page.get_title())
    home_page.page.go_back()

    logger.info("Navigate to Solutions Page")
    home_page.navigate_to("locations")
    assert ("Solutions" in location_page.get_title())
    home_page.page.go_back()

    logger.info("Navigate to Admin Page")
    home_page.navigate_to("admin_page")
    assert ("Administration" in admin_page.get_title())
    logger.info("Navigating to Admin Page is Successful")



