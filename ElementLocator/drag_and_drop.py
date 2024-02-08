import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragAndDrop:
    def drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.ID, "draggable")
        elem2 = driver.find_element(By.ID, "droppable")
        ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        #ActionChains(driver).drag_and_drop_by_offset(elem1, 110, 150).perform()
        time.sleep(5)


dd = DragAndDrop()
dd.drag_and_drop()
