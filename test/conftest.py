import pytest
from selenium import webdriver

from utilities import readConfigurations



@pytest.fixture()
def setup_and_teardown(request):
    browser = readConfigurations.read_configuration("basic_info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("provide a valid browser name")

    driver.maximize_window()
    app_url = readConfigurations.read_configuration("basic_info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()