from appium import webdriver

from test_Appium.po.page.base_page import BasePage
from test_Appium.po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["ensureWebviewsHavePages"] = True
            caps["noReset"] = "true"
            caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.launch_app()

        self.driver.implicitly_wait(8)

    def goto_main(self):
        return MainPage(self.driver)