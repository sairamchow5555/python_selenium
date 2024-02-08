import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementLocator:
    def locate_by_link_text(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        #driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
        driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for").click()
        time.sleep(5)


find_by_lint_text = ElementLocator()
find_by_lint_text.locate_by_link_text()
