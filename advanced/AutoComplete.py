from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class AutoComplete():
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)

        # Sent partial data
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        cityElement = driver.find_element_by_id('flight-origin-hp-flight')
        cityElement.send_keys('New York')
        time.sleep(3)

        # Find the item and click
        itemToSelect = driver.find_element_by_xpath("//div[@class='child-suggestion']//ap[contains(text(),'EWR')]")
        itemToSelect.click()
        time.sleep(3)
        
        driver.quit()

ff = AutoComplete()
ff.test()