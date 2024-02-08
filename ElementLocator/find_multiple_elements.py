import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementLocator:
    def find_elements(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.yatra.com/')
        #lista = driver.find_elements(By.TAG_NAME, 'a')
        lista = driver.find_elements(By.TAG_NAME, 'div')
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(5)


elements = ElementLocator()
elements.find_elements()
