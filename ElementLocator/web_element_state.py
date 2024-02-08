import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState:
    def enable_disable(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state1)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("sairam.chundru1432@gmail.com")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("sairam_5555")
        time.sleep(3)
        state2 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state2)
        time.sleep(5)


state_of_element = ElementState()
state_of_element.enable_disable()
