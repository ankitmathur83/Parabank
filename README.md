## Description
This project is to run two test cases as outlined in the file.

```
Application URL: https://parabank.parasoft.com/ 

Test case 1: UI Test scenarios:
1. Navigate to Para bank application.
2. Create a new user from user registration page (Ensure username is generated randomly and it is unique in every test execution).
3. Login to the application with the user created in step 2.
4. Create a Savings account from “Open New Account Page” and capture the account number.
5. Validate if Accounts overview page is displaying the balance details as expected.
6. Transfer funds from account created in step 5 to another account.
7. Pay the bill with account created in step 5.
8. Through API call using find transaction API call by amount for the payment done in step 7. (this covers API scenario as well)


Test case 2: Verify if the Global navigation menu in home page is working as expected.
1. Navigate to About Us Page
2. Navigating to Services Page is Successful
3. Navigate to Products Page
4. Navigate to Solutions Page
5. Navigate to Admin Page
```

## Techonologies Used:
```
Python
Playwright
Pytest Framework
Allure Report
```
### Prerequisites
```
python==3.12.0
playwright==1.50.0
pytest==8.3.4
allure-pytest==2.13.5
```


## Pytest
```
By default pytest runs on the all three browser. It can be controlled using conftest.py
pip install requirements.txt
pytest -s tests --alluredir=allure-results --maxfail=1 --disable-warnings -q

```
## Reports
```
allure serve ./allure-results
```
