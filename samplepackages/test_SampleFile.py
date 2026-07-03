import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
# @allure.severity(allure.severity_level.CRITICAL)
class TestLogin:


    driver=None

    @allure.severity(allure.severity_level.NORMAL)

    def test_ninja(self):

            self.driver.find_element(By.NAME,"search").send_keys("HP")
            self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
            status=self.driver.find_element(By.LINK_TEXT,"HP LP3065").text
            print("HP Product Display Status:", status)
            assert status
            # assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
            #allure.attach(self.driver.get_screenshot_as_png(), name="search_without_product",attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_ninja123(self):

        self.driver.find_element(By.NAME,"search").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
        expected_text="There is no product that matches the search criteria."
        status=self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        print("Product not avaible statius:", status)
        assert status
        #assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        #allure.attach(self.driver.get_screenshot_as_png(), name="search_without_product",attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_ninja1235555(self):

        self.driver.find_element(By.NAME,"search").send_keys("")
        self.driver.find_element(By.XPATH,"//button[contains(@class,'btn btn-default btn-lg')]").click()
        expected_text="There is no product that matches the search criteria."
        # status=self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        # print("Product not avaible statius12334:", status)
        # assert status
        assert self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
        #allure.attach(self.driver.get_screenshot_as_png(),name="search_without_product",attachment_type=AttachmentType.PNG)