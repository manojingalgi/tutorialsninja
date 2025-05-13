import pytest
from selenium.webdriver.common.by import By

from pages.Homepage import Homepage
from pages.Searchpage import Searchpage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        search_page = Searchpage(self.driver)
        assert search_page.display_status_of_valid_product()

    def test_search_for_a_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        search_page = Searchpage(self.driver)
        assert search_page.retrive_no_product_message() .__eq__(expected_text)

    def test_search_for_empty_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        search_page = Searchpage(self.driver)
        assert search_page.retrive_no_product_message().__eq__(expected_text)
