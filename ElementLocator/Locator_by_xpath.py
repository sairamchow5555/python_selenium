import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementLocator:
    def locate_by_xpath(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("sairam.chundru1432@gmail.com")
        time.sleep(5)


find_by_xpath = ElementLocator()
find_by_xpath.locate_by_xpath()
