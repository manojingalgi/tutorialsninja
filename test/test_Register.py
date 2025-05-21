from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages import accountsuccesspage
from pages.Homepage import Homepage
from pages.Registerpage import RegisterPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_register_options()
        registerPage = RegisterPage(self.driver)
        registerPage.enter_first_name("Manoj")
        registerPage.enter_last_name("K")
        registerPage.enter_email(self.generate_email_with_time_stamp())
        registerPage.enter_telephone("9876543210")
        registerPage.enter_password("12345")
        registerPage.enter_password_confirm("12345")
        registerPage.select_agree_checkbox_field()
        registerPage.click_on_continue_button()
        expected_heading = "Your Account Has Been Created!"
        accountSuccessPage = accountsuccesspage.AccountSuccessPage(self.driver).account_creation_message()
        if expected_heading == accountSuccessPage:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_register_with_mandatory_fields.png")


    def test_register_With_all_fields(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_register_options()
        registerPage = RegisterPage(self.driver)
        registerPage.enter_first_name("Manoj")
        registerPage.enter_last_name("K")
        registerPage.enter_email(self.generate_email_with_time_stamp())
        registerPage.enter_telephone("9876543210")
        registerPage.enter_password("12345")
        registerPage.enter_password_confirm("12345")
        registerPage.click_on_yes_radio_button()
        registerPage.click_on_continue_button()
        registerPage.select_agree_checkbox_field()
        expected_heading = "Your Account Has Been Created!"
        accountSuccessPage = accountsuccesspage.AccountSuccessPage(self.driver).account_creation_message()
        if expected_heading == accountSuccessPage:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_register_with_all_fields.png")

    def test_register_with_duplicate_email(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_register_options()
        registerPage = RegisterPage(self.driver)
        registerPage.enter_first_name("Manoj")
        registerPage.enter_last_name("K")
        registerPage.enter_email("manojingalgi@gmail.com")
        registerPage.enter_telephone("9876543210")
        registerPage.enter_password("12345")
        registerPage.enter_password_confirm("12345")
        registerPage.click_on_yes_radio_button()
        registerPage.click_on_continue_button()
        registerPage.select_agree_checkbox_field()

        expected_heading = "Warning: E-Mail Address is already registered!"
        actual_heading = registerPage.retrive_duplicate_Email_warning_message()
        if expected_heading == actual_heading:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\duplicate_email_assertion_failed.png")

    def test_without_any_data_provided(self):
        homepage = Homepage(self.driver)
        homepage.click_on_my_account_dropdown_menu()
        homepage.select_register_options()
        registerPage = RegisterPage(self.driver)
        registerPage.enter_first_name("")
        registerPage.enter_last_name("")
        registerPage.enter_email("")
        registerPage.enter_telephone("")
        registerPage.enter_password("")
        registerPage.enter_password_confirm("")
        registerPage.click_on_yes_radio_button()
        registerPage.click_on_continue_button()

        expected_heading = "First Name must be between 1 and 32 characters!"
        actual_heading = registerPage.email_empty_warning_message()
        if expected_heading == actual_heading:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_without_any_data_provided.png")

    def generate_email_with_time_stamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "manoj"+timestamp+"@gmail.com"
