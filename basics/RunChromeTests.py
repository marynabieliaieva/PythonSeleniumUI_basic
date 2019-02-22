from selenium import webdriver
import os

class RunChromeTests():
    def testMethodChrome(self):
        # Initiate the Chrome driver instance
        # Can comment the next 3 strings with executable path because the system variable was set
        #driverLocation = "D:\\selenium2019\\Chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = driverLocation
        #driver = webdriver.Chrome(driverLocation)
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")

chromeTest = RunChromeTests()
chromeTest.testMethodChrome()