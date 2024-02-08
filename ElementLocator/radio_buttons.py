import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class RadioButton:
    def click_radio_button(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        print(driver.find_element(By.XPATH, "//input[@value='Male']").is_selected())
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Male']").click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//input[@value='Male']").is_selected())
        print(driver.find_element(By.XPATH, "//input[@value='Female']").is_selected())
        driver.find_element(By.XPATH, "//input[@value='Female']").click()
        time.sleep(3)
        print(driver.find_element(By.XPATH, "//input[@value='Male']").is_selected())
        print(driver.find_element(By.XPATH, "//input[@value='Female']").is_selected())


radioButton = RadioButton()
radioButton.click_radio_button()
