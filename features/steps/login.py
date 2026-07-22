import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage
from utilities import EmailWithTimeStampGenerator


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page=HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page=context.home_page.select_login_option() ##opti


@when(u'I Enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context,email,password):
    #context.login_page=LoginPage(context.driver) ##optipip
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on Login button')
def step_impl(context):
    #context.login_page = LoginPage(context.driver)
    context.account_page=context.login_page.click_on_login_button() ##opti
    # context.login_page.click_on_login_button()
    #context.driver.find_element(By.XPATH,"//input[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    #context.account_page=AccountPage(context.driver) #opti basheer
    assert context.account_page.display_status_of_edit_your_account_information_option()



@when(u'I Enter invalid email address and valid password say "{password}" into the fields')
def step_impl(context,password):
    invalid_email=EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)

@then(u'I should get a proper warning message')
def step_impl(context):
    ##expected_warning_message="Warning: No match for E-Mail Address and/or Password." #opti
    ##context.login_page = LoginPage(context.driver)
    #assert context.login_page.retrieve_warning_message().__contains__("Warning: No match for E-Mail Address and/or Password.") #opti
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")



@when(u'I Enter valid email address say "{email}" and invalid password say "{password}" into the fields')
def step_impl(context,email,password):
    ##context.login_page=LoginPage(context.driver)
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I Enter invalid email address and invalid password say "{password}" into the fields')
def step_impl(context,password):
    invalid_email = EmailWithTimeStampGenerator.get_new_email_with_timestamp()
    ##context.login_page=LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    ##context.login_page=LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

#note: if homepage/login... created once and need to reuse use context.homepage or context.login if not error