import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Sliders:
    def sliders(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.snapdeal.com/products/mobiles-flip-cases-covers?sort=plrty&q=Price%3A179%2C599%7C")
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(elem1, 50, 0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset( 50, 0).release().perform()
        #ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset( 50, 0).release().perform()
        time.sleep(2)
        ActionChains(driver).drag_and_drop_by_offset(elem2, -70, 0).perform()
        time.sleep(3)


def main():
    sl = Sliders()
    sl.sliders()


main()
