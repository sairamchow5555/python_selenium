import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class BrowserMethods:
    def auto_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.rcvacademy.com/")
        print(driver.current_url)
        driver.maximize_window()
        print(driver.title)
        driver.find_element(By.LINK_TEXT, 'Login').click()
        driver.fullscreen_window()
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(3)
        driver.quit()


login = BrowserMethods()
login.auto_login()
