import time
from selenium import webdriver


class JavaScript:
    def javascript(self):
        driver = webdriver.Chrome()
        #driver.get("https://training.rcvacademy.com/courses")
        driver.execute_script("window.open('https://training.rcvacademy.com/courses', '_self');")
        time.sleep(5)
        element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(5)


js = JavaScript()
js.javascript()
