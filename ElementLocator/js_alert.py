import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class JavaScript_Alert:
    def js_alert(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)

        #Accept Alert
        # Alert(driver).accept()
        # time.sleep(3)

        #Dismiss Alert
        # Alert(driver).dismiss()
        # time.sleep(3)

        #Send Text to Alert
        Alert(driver).send_keys("Sairam")
        Alert(driver).accept()
        time.sleep(3)


pop_up = JavaScript_Alert()
pop_up.js_alert()
