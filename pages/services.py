import allure
import pytest

from pages.base_page import BasePage


class Services(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.account_number = None
        self.page_title = page.locator("#rightPanel title")
        self.open_new_account_link = page.get_by_role("link", name="Open New Account")
        self.account_dropdown = page.locator("#type")
        self.account_id_link = page.locator("#fromAccountId")
        self.open_new_account_button = page.get_by_role("button", name="Open New Account")
        self.new_account_id = page.locator("#newAccountId")
        self.account_open_status = page.locator("#openAccountResult h1")
        self.account_overview_link = page.get_by_role("link", name="Accounts Overview")
        self.account_overview_table_rows = page.locator("//tbody/tr")
        self.transfer_funds_link = page.get_by_role("link", name="Transfer Funds")
        self.amount_to_transfer_text = page.locator("#amount")
        self.from_account_transfer_dropdown = page.locator("#fromAccountId")
        self.to_account_transfer_dropdown = page.locator("#toAccountId")
        self.transfer_button = page.get_by_role("button", name="Transfer")
        self.transfer_complete_title = page.locator("#showResult h1")

        self.pay_bill_link = page.get_by_role("link", name="Bill Pay")
        self.payee_name_text = page.locator("input[name=\"payee\\.name\"]")
        self.payee_address_text = page.locator("input[name=\"payee\\.address\\.street\"]")
        self.payee_city_text = page.locator("input[name=\"payee\\.address\\.city\"]")
        self.payee_state_text = page.locator("input[name=\"payee\\.address\\.state\"]")
        self.payee_zipcode_text = page.locator("input[name=\"payee\\.address\\.zipCode\"]")
        self.payee_phone_number_text = page.locator("input[name=\"payee\\.phoneNumber\"]")
        self.payee_account_number_text = page.locator("input[name=\"payee\\.accountNumber\"]")
        self.verify_payee_account_number_text = page.locator("input[name=\"verifyAccount\"]")
        self.bill_amount_text = page.locator("input[name=\"amount\"]")
        self.pay_from_account = page.locator("select[name=fromAccountId]")
        self.send_payment_button = page.get_by_role("button", name="Send Payment")
        self.bill_payment_status = page.locator("#billpayResult h1")

    @allure.step("validate Services title")
    def get_title(self):
        return self.page_title.text_content()

    @allure.step("Open a Savings Account")
    def open_savings_account(self, account_type):
        self.open_new_account_link.click()
        self.page.wait_for_timeout(3000)
        if account_type == "SAVINGS":
            self.account_dropdown.select_option(label="SAVINGS")
        else:
            self.account_id.select_text(label="CHECKING")
        self.open_new_account_button.click()
        self.page.wait_for_selector("#newAccountId", state="visible")
        self.account_number = self.new_account_id.text_content()
        return self.account_number

    def open_account_status(self):
        return self.account_open_status.text_content()

    def account_overview(self, account_number):
        self.account_overview_link.click()
        self.page.wait_for_timeout(3000)
        balance = (self.account_overview_table_rows.locator(":scope", has_text=account_number)
                   .locator("//td[2]")).text_content()
        return balance

    def transfer_funds_from_account(self, account_number: str, amount_to_transfer: str):
        self.transfer_funds_link.click()
        self.amount_to_transfer_text.fill(amount_to_transfer)
        self.from_account_transfer_dropdown.select_option(label=account_number)
        self.to_account_transfer_dropdown.select_option(index=1)
        self.transfer_button.click()
        return self.transfer_complete_title.text_content()

    def pay_bill(self, payee_name=None, address_street=None, payee_city=None, payee_state=None,
                 payee_zipcode=None, payee_phone_number=None, payee_account=None, bill_amount=None,
                 account_number=None):
        self.pay_bill_link.click()
        self.payee_name_text.fill(payee_name)
        self.payee_address_text.fill(address_street)
        self.payee_city_text.fill(payee_city)
        self.payee_state_text.fill(payee_state)
        self.payee_zipcode_text.fill(payee_zipcode)
        self.payee_phone_number_text.fill(payee_phone_number)
        self.payee_account_number_text.fill(payee_account)
        self.verify_payee_account_number_text.fill(payee_account)
        self.bill_amount_text.fill(bill_amount)
        self.pay_from_account.select_option(label=account_number)
        self.send_payment_button.click()
        return self.bill_payment_status.text_content()
