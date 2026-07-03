import time

import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    driver=None

    def test_create_account_with_man_filed(self):

        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("abc")
        self.driver.find_element(By.ID, "input-lastname").send_keys("xyz")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("98765432310")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        # status= driver.find_element(By.XPATH,"//div[@id='content']/h1").text
        # print("test_content:",status)
        # assert status


    def test_create_account_with_man_all_filed(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("abc")
        self.driver.find_element(By.ID, "input-lastname").send_keys("xyz")
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, "input-telephone").send_keys("98765432310")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_text="Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)
        # status= driver.find_element(By.XPATH,"//div[@id='content']/h1").text
        # print("test_content:",status)
        # assert status



    def generate_email_time_stamp(self):
        timestamp=  time.strftime('%Y_%m_%d_%H_%M_%S')
        #timestamp=  timestamp.replace('-','_').replace(' ','_').replace(':','_')
        return "arun"+timestamp+"@gmail.com"