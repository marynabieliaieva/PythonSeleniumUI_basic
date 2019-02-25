from selenium import webdriver

class Screenshots():
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(baseUrl)

        destinationFileName = "D:\\books\\1.png"

        try:
            driver.save_screenshot(destinationFileName)
            print('ok')
        except NotADirectoryError:
            print('not ok')

        driver.quit()
ff = Screenshots()
ff.test()