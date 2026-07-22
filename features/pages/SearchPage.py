from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchPage(BasePage):

    #constructor
    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    valid_product_link_text="HP LP3065"
    message_xpath="//input[@id='button-search']/following-sibling::p"

    #action_methods
    def display_status_of_product(self):
        return self.display_status("valid_product_link_text",self.valid_product_link_text)  #return ?
        #return self.driver.find_element(By.LINK_TEXT,self.valid_product_link_text).is_displayed()

    def display_status_of_message(self,expected_message_text):
        return self.retrieved_element_text_equals("message_xpath",self.message_xpath,expected_message_text) #return?
        #return self.driver.find_element(By.XPATH,self.message_xpath).text.__eq__(expected_message_text)