from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
java_error=driver.find_element(By.ID,"ta1")


driver.execute_script("arguments[0.value='basheer'",java_error)


time.sleep(5)
driver.quit()
