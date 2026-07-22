from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class AccountPage(BasePage):

    #constructor
    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    edit_your_account_information_option_link_text="Edit your account information"

    #actions_methods
    def display_status_of_edit_your_account_information_option(self):
        return self.display_status("edit_your_account_information_option_link_text",self.edit_your_account_information_option_link_text)
        #return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_information_option_link_text).is_displayed()