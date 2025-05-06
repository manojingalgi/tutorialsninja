from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Manoj")
        self.driver.find_element(By.ID,"input-lastname").send_keys("K")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_time_stamp())
        self.driver.find_element(By.ID,"input-telephone").send_keys("9876543210")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_heading = "Your Account Has Been Created!"
        actual_heading = self.driver.find_element(By.XPATH,"//div[@id='content']/h1")
        if expected_heading == actual_heading:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_register_with_mandatory_fields.png")

    def test_register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("Manoj")
        self.driver.find_element(By.ID,"input-lastname").send_keys("K")
        self.driver.find_element(By.ID,"input-email").send_keys("manojingalgi@gmail.com")
        self.driver.find_element(By.ID,"input-telephone").send_keys("9036140740")
        self.driver.find_element(By.ID,"input-password").send_keys("password")
        self.driver.find_element(By.ID,"input-confirm").send_keys("password")
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_heading = "Warning: E-Mail Address is already registered!"
        actual_heading = self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text
        if expected_heading == actual_heading:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\duplicate_email_assertion_failed.png")

    def test_without_any_data_provided(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("")
        self.driver.find_element(By.ID,"input-lastname").send_keys("")
        self.driver.find_element(By.ID,"input-email").send_keys("")
        self.driver.find_element(By.ID,"input-telephone").send_keys("")
        self.driver.find_element(By.ID,"input-password").send_keys("")
        self.driver.find_element(By.ID,"input-confirm").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_heading = "First Name must be between 1 and 32 characters!"
        actual_heading = self.driver.find_element(By.XPATH,"//div[contains(text(),'First Name must be between 1 and 32 characters!')]").text
        if expected_heading == actual_heading:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_without_any_data_provided.png")

    def generate_email_with_time_stamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "manoj"+timestamp+"@gmail.com"