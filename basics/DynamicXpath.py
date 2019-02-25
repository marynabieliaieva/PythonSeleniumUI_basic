from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicXpath():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Login
        driver.find_element_by_link_text('Login').click()
        driver.find_element_by_id('user_email').send_keys('test@email.com')
        driver.find_element_by_id('user_password').send_keys('abcabc')
        driver.find_element_by_name('commit').click()

        # Search for courses
        driver.find_element_by_id('search-courses').send_keys('JavaScript')
        driver.find_element_by_id('search-course-button').click()

        # Select cource

        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

ff=DynamicXpath()
ff.test()