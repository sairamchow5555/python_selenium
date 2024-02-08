from selenium import webdriver
from selenium.webdriver.common.by import By


class ImplicitWait:
    def implicit_wait(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "username").send_keys("sairam.chundru1432@gmail.com")
        driver.find_element(By.ID, "password").send_keys("sairam")


iml_w = ImplicitWait()
iml_w.implicit_wait()
