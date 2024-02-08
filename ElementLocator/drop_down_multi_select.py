import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown:
    def multi_select(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
        dd_demo = driver.find_element(By.NAME, "selenium_commands")
        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(0)
        dd_multi.select_by_visible_text("Navigation Commands")
        dd_multi.select_by_visible_text("Switch Commands")
        time.sleep(5)
        dd_multi.deselect_by_index(2)
        time.sleep(5)
        dd_multi.deselect_all()
        time.sleep(5)
        # for i in range(5):
        #     dd_multi.select_by_index(i)
        #     time.sleep(2)


drop_down_multi_select = DropDown()
drop_down_multi_select.multi_select()
