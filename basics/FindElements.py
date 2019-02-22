from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElements():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        elementByName = driver.find_element_by_name("show-hide")
        elementByCss = driver.find_element_by_css_selector("#benzcheck")
        elementByCss1 = driver.find_element_by_css_selector("input[id='displayed-text']")
        elementByCss2 = driver.find_element_by_css_selector("button[class='btn-style class1']")
        # If class name has space inside, use . instead of space
        elementByCss3 = driver.find_element_by_css_selector(".btn-style.class1")
        elements = driver.find_elements(By.CSS_SELECTOR, '.left-align')
        wildCardsElement1 = driver.find_element_by_css_selector("div[class^='block']")
        wildCardsElement2 = driver.find_element_by_css_selector("div[class$='align']")
        wildCardsElement3 = driver.find_element_by_css_selector("button[class*='style']")
        childElement1 = driver.find_element_by_css_selector("fieldset>a#opentab")
        childElement2 = driver.find_element_by_css_selector("fieldset>a.class1")



        if childElement1 is not None:
            print('Found')

        if childElement2 is not None:
            print('Found')

        driver.get("https://google.com")
        elementByXpath = driver.find_element_by_xpath("//*[contains(@name, 'btn')]")



ff = FindElements()
ff.test()