from selenium import webdriver
from selenium.webdriver.common.by import By
from basics.HandyWrappers import HandyWrappers

class UsingWrappers:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        hw = HandyWrappers(driver)
        driver.implicitly_wait(3)

        textField = hw.getElement('name')
        textField.send_keys('test')

        elementResult = hw.getElement('name', By.ID)
        print(str(elementResult))

        elementResult1 = hw.getElement("//input[@id='name1']", By.XPATH)
        print(str(elementResult1))

        driver.quit()

ff = UsingWrappers()
ff.test()