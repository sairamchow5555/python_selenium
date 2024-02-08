import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class RightClickAndDoubleClick:
    def rightclick_and_doubleclick(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        achains = ActionChains(driver)

        #Right Click
        elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        achains.context_click(elem1).perform()
        time.sleep(3)
        copyelem.click()
        time.sleep(3)
        Alert(driver).accept()
        time.sleep(2)

        #Double Click
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(elem2).perform()
        time.sleep(3)
        Alert(driver).accept()
        time.sleep(2)


rc_and_dc = RightClickAndDoubleClick()
rc_and_dc.rightclick_and_doubleclick()
