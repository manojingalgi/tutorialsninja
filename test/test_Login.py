import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    driver.find_element(By.ID,"input-email").send_keys("manojingalgi@gmail.com")
    driver.find_element(By.ID,"input-password").send_keys("password")
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    assert driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
    driver.quit()

def test_login_with_invalid_email_and_valid_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_time_stamp())
    driver.find_element(By.ID, "input-password").send_keys("password")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(5)
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_message)
    driver.quit()

def generate_email_with_time_stamp():

    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "manoj"+timestamp+"@gmail.com"


def test_login_with_valid_email_and_invalid_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("manojingalgi@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("qwerty")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(5)
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_message)
    driver.quit()

def test_login_without_credentails():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(5)
    expected_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(expected_message)
    driver.quit()