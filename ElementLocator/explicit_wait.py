import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class DateSelection:
    def auto_suggest_dropdown(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(5)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(5)

        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        #print(len(search_result))
        for results in search_result:
            #print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(5)
                break

        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(5)

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveID']")
        for date in all_dates:
            if date.get_attribute("data-date") == "30/09/2023":
                date.click()
                time.sleep(5)
                break


auto_suggest = DateSelection()
auto_suggest.auto_suggest_dropdown()
