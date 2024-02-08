import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText:
    def find_text(self):
        driver = webdriver.Chrome()
        driver.get("https://in.bookmyshow.com/explore/home/hyderabad")
        text1 = driver.find_element(By.XPATH, "//div[contains(text(),'Miss Shetty Mr Polishetty')]").text
        print(text1)
        text2 = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1)").text
        print(text2)
        time.sleep(5)


find_get_text = GetText()
find_get_text.find_text()
