from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self,driver):
        self.driver = driver
    first_name_field_id ="input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_message_xpath = "//div[@id='content']/h1"
    email_empty_warning_message_xpath = "//div[contains(text(),'First Name must be between 1 and 32 characters!')]"

    def enter_first_name(self,first_name_text):
        self.driver.find_element(By.ID,self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self,last_name_text):
        self.driver.find_element(By.ID,self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_id).click()
        self.driver.find_element(By.ID, self.telephone_id).clear()
        self.driver.find_element(By.ID, self.telephone_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_password_confirm(self, password_text):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(password_text)

    def select_agree_checkbox_field(self):
        self.driver.find_element(By.NAME, self.agree_field).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self.continue_button_xpath).click()

    def click_on_yes_radio_button(self):
        self.driver.find_element(By.XPATH,self.yes_radio_button).click()


    def retrive_duplicate_Email_warning_message(self):
        return self.driver.find_element(By.XPATH,self.duplicate_email_warning_message_xpath).text

    def email_empty_warning_message(self):
        return self.driver.find_element(By.XPATH,self.email_empty_warning_message_xpath).text