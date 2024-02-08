import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class ScreenShot:
    def demo_screen_shot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)
        driver.get_screenshot_as_file("pic1.png")
        dd_continue = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        dd_continue.click()
        time.sleep(3)
        driver.get_screenshot_as_file("pic2.png")
        time.sleep(3)
        driver.save_screenshot("pic3.png")
        time.sleep(3)


yatra_screen_shot = ScreenShot()
yatra_screen_shot.demo_screen_shot()
