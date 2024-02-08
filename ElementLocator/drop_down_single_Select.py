import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDownSingleSelect:
    def single_select(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        time.sleep(3)
        driver.find_element(By.NAME, "UserFirstName").send_keys("sairam")
        time.sleep(2)
        driver.find_element(By.NAME, "UserLastName").send_keys("chundru")
        time.sleep(2)

        dropdown = driver.find_element(By.NAME, "UserTitle")

        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)

        dd.select_by_value("Customer_Service_Manager_ANZ")
        time.sleep(3)


drop_down = DropDownSingleSelect()
drop_down.single_select()
