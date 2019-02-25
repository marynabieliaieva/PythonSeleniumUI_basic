from selenium import webdriver
from selenium.webdriver import ActionChains
import time

class DragAndDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        fromElement = driver.find_element_by_id('draggable')
        toElement = driver.find_element_by_id('droppable')
        time.sleep(3)

        try:
            actions = ActionChains(driver)
            actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
            print('Drag and Drop successful')
            time.sleep(3)
        except:
            print('Drag and drop failed')

        driver.quit()
ff = DragAndDrop()
ff.test()