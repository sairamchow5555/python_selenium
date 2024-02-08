import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckBoxes:
    def click_checkboxes(self):
        driver = webdriver.Chrome()
        #driver.get("https://www.yatra.com/")
        # driver.find_element(By.CSS_SELECTOR, "a[title='Non Stop Flights']").click()
        # time.sleep(3)
        # var1 = driver.find_element(By.CSS_SELECTOR, "a[title='Non Stop Flights']").is_selected()
        # print(var1)
        # time.sleep(2)
        #driver.find_element(By.ID, "special_student_offer").click()
        #time.sleep(3)
        # driver.find_element(By.ID, "armedforces_offers").click()
        # time.sleep(2)
        # var2 = driver.find_element(By.ID, "armedforces_offers").is_selected()
        # print(var2)
        # time.sleep(3)
        # driver.get("https://www.sugarcrm.com/au/request-demo/")
        # driver.maximize_window()
        # # var3 = driver.find_element(By.ID, "doi0").is_selected()
        # # print(var3)
        # time.sleep(3)
        # driver.find_element(By.ID,"doi0").click()
        # time.sleep(3)
        # var4 = driver.find_element(By.ID, "doi0").is_selected()
        # print(var4)
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        print(driver.find_element(By.XPATH, "//input[@value='Manual Tester']").is_selected())
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@value='Manual Tester']").click()
        time.sleep(4)
        print(driver.find_element(By.XPATH, "//input[@value='Manual Tester']").is_selected())


click_on_checkboxes = CheckBoxes()
click_on_checkboxes.click_checkboxes()
