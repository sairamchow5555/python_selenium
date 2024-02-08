import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementLocator:
    def locate_by_tagname_and_classname(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        #driver.find_element(By.TAG_NAME, "input").send_keys('sairam.chundru1432@gmail.com')
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys('sairam.chundru1432@gmail.com')
        time.sleep(5)


find_by_tagname_and_classname = ElementLocator()
find_by_tagname_and_classname.locate_by_tagname_and_classname()
