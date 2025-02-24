import pytest
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage

import requests


class Transaction_API(BasePage):

    def __init__(self, page):
        # Base URL for the Parabank API
        super().__init__(page)
        self.api_request_context = page
        self.API_BASE_URL = "https://parabank.parasoft.com/parabank/services_proxy/bank/accounts/"

    def get_account_transactions_by_amount(self, account_id: str, amount: str):
        """API request to Find by Amount

        Args:
            account_id (str): accountid for which this request to be made.
            amount (str): amount which needed to be searched.

        Returns:
            json: API response of returned call.
        """
        url = self.API_BASE_URL + account_id + "/transactions/amount/" + amount
        api_context = self.api_request_context.request
        api_response = api_context.get(url)
        print(api_response.json())
        # Assert on the API response
        assert api_response.status == 200 # Check that the status code is 200
        return api_response.json()