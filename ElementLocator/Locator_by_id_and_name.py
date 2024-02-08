import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementLocator:
    def locate_by_id_and_name(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        #driver.find_element(By.ID, 'login-input').send_keys('sairam.chundru1432@gmail.com')
        driver.find_element(By.NAME, 'login-input').send_keys('sairam.chundru1432@gmail.com')
        time.sleep(5)


findbyid = ElementLocator()
findbyid.locate_by_id_and_name()
