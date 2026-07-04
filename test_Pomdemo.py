from selenium import webdriver
from selenium.webdriver.common.by import By
from LoginPageObjects import LoginPage
import pytest

class TestLogin:

    def test_login(self):
        self.driver=webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://admin-demo.nopcommerce.com/login")


        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickloginpage()
        self.act_title=self.driver.title

        assert self.act_title=="Dashboard / nopCommerce administration"
        self.driver.close()



