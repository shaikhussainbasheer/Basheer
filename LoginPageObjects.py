from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    #locators-https://admin-demo.nopcommerce.com/login
    textbox_uesrname_id="Email"
    textbox_paasword_id="Password"
    button_login_xpath="//button[text()='Log in']"

    #constructor
    def __init__(self,driver):
        self.driver=driver



    #actions methods
    def setUserName(self,username):
        username_txt=self.driver.find_element(By.ID,self.textbox_uesrname_id)#identify element
        username_txt.clear()
        username_txt.send_keys(username)

    def setPassword(self,password):
        passwordtxt=self.driver.find_element(By.ID,self.textbox_paasword_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def clickloginpage(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()


