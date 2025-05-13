import time
from datetime import datetime

import pytest

from pages.Homepage import Homepage
from pages.Loginpage import LoginPage
from pages.accountsPage import AccountsPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def __init__(self):
        self.driver = None

    def test_login_with_valid_credentials(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_login_option()
        LoginPage(self.driver)
        LoginPage.enter_email_address("manojingalgi@gmail.com")
        LoginPage.enter_password_text("password")
        LoginPage.click_on_Login_button()
        account_page  = AccountsPage(self.driver)

        assert account_page.display_status_edit_your_account_info()

    def test_login_with_invalid_email_and_valid_password(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_login_option()
        LoginPage(self.driver)
        LoginPage.enter_email_address(self.generate_email_with_time_stamp())
        LoginPage.enter_password_text("password")
        LoginPage.click_on_Login_button()
        time.sleep(5)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert LoginPage.retrive_warning_message().__contains__(expected_message)

    def generate_email_with_time_stamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "manoj"+timestamp+"@gmail.com"

    def test_login_with_valid_email_and_invalid_password(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_login_option()
        LoginPage(self.driver)
        LoginPage.enter_email_address("manojingalgi@gmail.com")
        LoginPage.enter_password_text("manoj")
        LoginPage.click_on_Login_button()
        time.sleep(5)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert LoginPage.retrive_warning_message().__contains__(expected_message)

    def test_login_without_credentails(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_login_option()
        LoginPage(self.driver)
        LoginPage.enter_email_address("")
        LoginPage.enter_password_text("")
        LoginPage.click_on_Login_button()
        time.sleep(5)
        expected_message = "Warning: No match for E-Mail Address and/or Password."
        assert LoginPage.retrive_warning_message().__contains__(expected_message)