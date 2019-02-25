from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class Sliders():
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        element = driver.find_element_by_xpath("//div[@id='slider']//span")
        time.sleep(3)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 500, 0)
            print('Sliding is successful')
            time.sleep(3)
        except:
            print('Sliding failed')

        #driver.quit()
ff = Sliders()
ff.test()