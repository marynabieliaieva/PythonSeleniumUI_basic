from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class JavaScriptExecution():
    def test(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        element = driver.execute_script("return document.getElementById('name');")


        # Get height and width values
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print('Height: ' + str(height))
        print('Width: ' + str(width))


        # Scroll down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(10)

        # Scroll up
        driver.execute_script("window.scrollBy(0, -1000);")
        driver.quit()

        # Scroll element into view
        element = driver.find_element_by_id('mouseover')
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")

ff = JavaScriptExecution()
ff.test()
