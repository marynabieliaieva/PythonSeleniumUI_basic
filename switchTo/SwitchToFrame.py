from selenium import webdriver
import time

class SwitchToFrame():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()


        # Switch to frame using ID
        driver.switch_to.frame('courses-iframe')
        time.sleep(3)
        searchBox = driver.find_element_by_id('search-courses')
        searchBox.send_keys('python')
        time.sleep(3)

        # Switch back to parent window
        driver.switch_to.default_content()
        driver.find_element_by_id('name').send_keys('test')

ff = SwitchToFrame()
ff.test()