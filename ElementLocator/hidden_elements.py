import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class HiddenElement:
    def is_displayed(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)
        elem2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem2)

    # def is_displayed_yatra(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.yatra.com/")
    #     driver.find_element(By.XPATH, "//span[@class='flight_cls']").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//div[@data-flightagegroup='child']//span[@class='ddSpinnerPlus']").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//span[@class='ddSpinnerMinus']").click()
    #     time.sleep(2)


find_hidden_element = HiddenElement()
find_hidden_element.is_displayed()
