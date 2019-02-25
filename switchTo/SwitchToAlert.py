from selenium import webdriver
import time

class SwitchToAlert():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()

        driver.find_element_by_id('name').send_keys('test')
        driver.find_element_by_id('alertbtn').click()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)
        driver.find_element_by_id('name').send_keys('test')
        driver.find_element_by_id('confirmbtn').click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(3)
        driver.quit()




ff = SwitchToAlert()
ff.test()