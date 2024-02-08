import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class AutoSuggest:
    def auto_suggest_dropdown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(5)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(5)

        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            print(results.text)
            if "New Haven (HVN)" in results.text:
                results.click()
                time.sleep(5)
                break


auto_suggest = AutoSuggest()
auto_suggest.auto_suggest_dropdown()
