import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MouseOver:
    def mouse_over(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        myaccount_link = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        more_button = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achains = ActionChains(driver)
        # achains.move_to_element(myaccount_link)
        # achains.perform()
        achains.move_to_element(myaccount_link).perform()
        time.sleep(3)
        achains.move_to_element(more_button).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[@class='demo-icon icon-xplore']").click()
        time.sleep(3)


mo = MouseOver()
mo.mouse_over()
