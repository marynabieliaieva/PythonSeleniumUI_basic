from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.ExplicitWaitType import ExplicitWaitType
import time
from selenium.webdriver.common.keys import Keys

class CalendarSection():
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        departingField = driver.find_element(By.ID, "flight-departing-hp-flight")
        departingField.click()
        departingDay = driver.find_element_by_xpath("//button[@class='datepicker-cal-date'][@data-month='2'][@data-day='24']")
        departingDay.click()
        time.sleep(10)






        driver.quit()




ff=CalendarSection()
ff.test()