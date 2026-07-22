from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountSuccessPage(BasePage):


    #constructor
    def __init__(self,driver):
        super().__init__(driver)

    #Locators

    account_creation_message_xpath="//div[@id='content']/h1"


    #actions_methods
    def display_status_of_account_created_heading(self,expected_heading):
        return self.retrieved_element_text_equals("account_creation_message_xpath",self.account_creation_message_xpath,expected_heading)
        #return self.driver.find_element(By.XPATH,self.account_creation_message_xpath).text.__eq__(expected_heading)
