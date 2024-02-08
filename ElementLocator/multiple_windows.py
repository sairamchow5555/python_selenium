import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class MultipleWindows:
    def multiple_windows(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        parent_handler = driver.current_window_handle
        print(parent_handler)
        driver.find_element(By.XPATH, "//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        time.sleep(5)
        all_handlers = driver.window_handles
        print(all_handlers)
        #driver.switch_to.window(all_handlers[1])
        for handler in all_handlers:
            if handler != parent_handler:
                driver.switch_to.window(handler)
                driver.find_element(By.XPATH, "//a[normalize-space()='customer care']").click()
                time.sleep(5)

        time.sleep(5)


multiple = MultipleWindows()
multiple.multiple_windows()
