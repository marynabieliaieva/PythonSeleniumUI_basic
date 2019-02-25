from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class MouseHovering():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()

        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(3)
        element = driver.find_element_by_id('mousehover')
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('Mouse is hovered')
            time.sleep(3)
            topLink = driver.find_element_by_xpath(itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print('item is clicked')
        except:
            print('Mouse failed')



ff = MouseHovering()
ff.test()