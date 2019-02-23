from selenium import webdriver
import os


class RunFFTests():
    def testMethodFF(self):
    # Initiate the Firefox driver instance
    # Can comment the next string with executable path because the system variable was set
    #   driver = webdriver.Firefox(executable_path="D:\\selenium2019\\geckodriver.exe")

        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")
        driver.quit()

ff=RunFFTests()
ff.testMethodFF()

