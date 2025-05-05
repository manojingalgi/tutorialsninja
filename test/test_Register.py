import time
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be


def test_register_with_mandatory_fields():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("Manoj")
    driver.find_element(By.ID,"input-lastname").send_keys("K")
    driver.find_element(By.ID,"input-email").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.ID,"input-telephone").send_keys("9876543210")
    driver.find_element(By.ID,"input-password").send_keys("12345")
    driver.find_element(By.ID,"input-confirm").send_keys("12345")
    driver.find_element(By.ID,"//input[@name='agree']").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_heading = "Your Account Has Been Created!"
    actual_heading = driver.find_element(By.XPATH,"//div[@id='content']/h1")
    if expected_heading == actual_heading:
        assert True
        driver.quit()
    else:
        driver.save_screenshot(".\\screenshots\\test_register_with_mandatory_fields.png")
        driver.quit()


def test_register_with_duplicate_email():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("Manoj")
    driver.find_element(By.ID,"input-lastname").send_keys("K")
    driver.find_element(By.ID,"input-email").send_keys("manojingalgi@gmail.com")
    driver.find_element(By.ID,"input-telephone").send_keys("9036140740")
    driver.find_element(By.ID,"input-password").send_keys("password")
    driver.find_element(By.ID,"input-confirm").send_keys("password")
    driver.find_element(By.XPATH,"//input[@name='agree']").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_heading = "Warning: E-Mail Address is already registered!"
    actual_heading = driver.find_element(By.XPATH,"//div[@id='content']/h1").text
    if expected_heading == actual_heading:
        assert True
        driver.quit()
    else:
        driver.save_screenshot(".\\screenshots\\duplicate_email_assertion_failed.png")
        driver.quit()

def test_without_any_data_provided():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("")
    driver.find_element(By.ID,"input-lastname").send_keys("")
    driver.find_element(By.ID,"input-email").send_keys("")
    driver.find_element(By.ID,"input-telephone").send_keys("")
    driver.find_element(By.ID,"input-password").send_keys("")
    driver.find_element(By.ID,"input-confirm").send_keys("")
    driver.find_element(By.XPATH,"//input[@name='agree']").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_heading = "Warning: E-Mail Address is already registered!"
    actual_heading = driver.find_element(By.XPATH,"//div[@id='content']/h1").text
    if expected_heading == actual_heading:
        assert True
        driver.quit()
    else:
        driver.save_screenshot(".\\screenshots\\test_without_any_data_provided.png")
        driver.quit()






















def generate_email_with_time_stamp():

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "manoj"+timestamp+"@gmail.com"


#//div[@id='account-register']/div[1]