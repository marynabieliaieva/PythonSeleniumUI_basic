from selenium import webdriver
class BrowserInteraction():
    def test(self):
        baseUrl="https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()

        # Window maximize
        driver.maximize_window()

        # Open the URL
        driver.get(baseUrl)

        # Get title
        print(driver.title)

        # Get current url
        print(driver.current_url)

        # Browser refresh
        driver.refresh()

        # Open another URL
        print(driver.get(driver.current_url))

        # Browser back
        driver.back()

        # Browser Forward
        driver.forward()

        # Get page Source
        print(driver.page_source)

        # Browser Close / Quit
        driver.quit()


ff=BrowserInteraction()
ff.test()