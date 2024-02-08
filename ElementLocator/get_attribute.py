import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetAttribute:
    def find_attribute(self):
        driver = webdriver.Chrome()
        # driver.get("https://www.yatra.com/")
        # attr1 = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("class")
        # print(attr1)
        # attr2 = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("type")
        # print(attr2)
        # attr3 = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        # print(attr3)
        driver.get("https://www.ixigo.com/flights")
        attr4 = driver.find_element(By.XPATH, "//img[@title='IPHONE WEB']").get_attribute("title")
        print(attr4)
        time.sleep(5)


attr_obj = GetAttribute()
attr_obj.find_attribute()
