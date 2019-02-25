from selenium import webdriver
import time

class SwitchToWindow():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.maximize_window()

        # Find parent Window
        parentHandle = driver.current_window_handle

        # Find button and click it
        driver.find_element_by_id('openwindow').click()
        time.sleep(3)

        # Find all windows
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print(handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to " + handle)
                searchBox = driver.find_element_by_id('search-courses')
                searchBox.send_keys('python')
                time.sleep(3)
                driver.close()

        # Switch back to the parent window
        driver.switch_to.window(parentHandle)
        driver.find_element_by_id('name').send_keys('test')

        driver.quit()

        #


ff = SwitchToWindow()
ff.test()