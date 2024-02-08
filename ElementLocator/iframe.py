import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class IFrame:
    def iframe(self):
        driver = webdriver.Chrome()
        driver.fullscreen_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        #switch with iframe locator
        #driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))

        #switch with ID
        driver.switch_to.frame("iframeResult")

        #switch with Name
        #driver.switch_to.frame("iframeResult")

        #switching with index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//div[@class='tnb-right-section']//a[5]").click()
        time.sleep(5)


inline_iframe = IFrame()
inline_iframe.iframe()
