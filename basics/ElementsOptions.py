from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

class ElementsOptions():
    def elementsOptions(self):
        baseUrl="https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Verify if element is enabled.
        textField=driver.find_element(By.ID, 'displayed-text')
        textFieldState = textField.is_enabled()

        if textFieldState is not None:
            print('Is element enabled? ' + str(textFieldState))


        # Check if radiobutton is selected. If not, select it.
        radioButtonBMW = driver.find_element_by_id('bmwradio')

        if radioButtonBMW.is_selected():
            print('BMV already selected')
        else:
            radioButtonBMW.click()

        # Define list of the checkboxes. Check all checkboxes from the list.
        checkboxesCars = driver.find_elements_by_xpath("//input[contains(@type, 'checkbox')and contains(@name, 'cars')]")

        size = len(checkboxesCars)
        print('Size of the list: ' + str(size))

        for checkbox in checkboxesCars:
            isSelected = checkbox.is_selected()

            if not isSelected:
                checkbox.click()

        # Define dropdown list and select items by different ways.
        selectList = driver.find_element_by_id('carselect')
        selectedElement = Select(selectList)

        selectedElement.select_by_value('honda')
        selectedElement.select_by_index(0)
        selectedElement.select_by_visible_text('Benz')

        # Find the state of the text box, switch to another state and verify the state changes
        textBoxElement = driver.find_element_by_id('displayed-text')
        hideButton = driver.find_element_by_id('hide-textbox')
        textBoxState = textBoxElement.is_displayed()
        if textBoxState is True:
            hideButton.click()
        else:
            return False

        textBoxState = textBoxElement.is_displayed()
        assert textBoxState is False
        driver.quit()


e=ElementsOptions()
e.elementsOptions()