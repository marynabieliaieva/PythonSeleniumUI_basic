from selenium import webdriver
import os

class RunIETests():
    def testMethodIE(self):
        # Initiate the Chrome driver instance
        # be sure that zoom for ie = 100%
        # In the IE settings> security tab uncheck safe mode for all zones
        # Can comment the next 3 strings with executable path because the system variable was set
        # driverLocation = "D:\\selenium2019\\IEDriverServer.exe"
        # os.environ["webdriver.ie.driver"] = driverLocation
        # driver = webdriver.Ie(driverLocation)
        driver = webdriver.Ie()
        driver.get("http://www.letskodeit.com")
        driver.quit()

ieTest = RunIETests()
ieTest.testMethodIE()