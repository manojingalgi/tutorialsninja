from selenium.webdriver.common.by import By


class AccountsPage:
    def __init__(self,driver):
        self.driver = driver
    edit_your_account_information_option_1ink_text ="Edit your account information"

    def display_status_edit_your_account_info(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_information_option_1ink_text).is_displayed()

