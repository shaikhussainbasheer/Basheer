import pytest
from selenium.webdriver.common.by import By
import allure


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    driver=None


    def test_login_with_valid_cred(self):

        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("viratkohli8919@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("Virat@18")
        self.driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()
        expected_content="Edit your account information"
        # login_status=driver.find_element(By.LINK_TEXT,"Edit your account information").text
        # print("Login success status:",login_status)
        # assert login_status
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").text.__eq__(expected_content)



    def test_login_with_invalid_cred(self):

        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("")
        self.driver.find_element(By.ID,"input-password").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()
        expected_content="Warning: No match for E-Mail Address and/or Password."
        # login_status=driver.find_element(By.XPATH,"//div[contains(text(),'Warning: No match for E-Mail Address and/or Password.')]").text
        # print("Login success status:",login_status)
        # assert login_status
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Warning: No match for E-Mail Address and/or Password.')]").text.__contains__(expected_content)
