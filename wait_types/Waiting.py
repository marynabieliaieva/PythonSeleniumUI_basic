from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import time

class Waiting():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Login
        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('user_email').send_keys('test@email.com')
        driver.find_element_by_id('user_password').send_keys('abcabc')
        driver.find_element_by_name('commit').click()


        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=
        [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])

        element = wait.until(EC.element_to_be_clickable((By.ID, "search-course-button")))
        element.click()

        driver.quit()

ff=Waiting()
ff.test()