from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.pull-right.btn-lg")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        driver.quit()

ff = ImplicitWaitDemo()
ff.test()