from selenium import webdriver

class GetValues():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Grab a text of the elements
        openTabElement = driver.find_element_by_id('opentab')
        elementText=openTabElement.text
        print(elementText)

        # Grab the attributes value of the elements
        nameTextField = driver.find_element_by_id('name')
        placeholder = nameTextField.get_attribute('placeholder')
        print(placeholder)

        driver.quit()

ff = GetValues()
ff.test()