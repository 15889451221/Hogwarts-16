from appium import webdriver

from test_Appium.po.page.base_page import BasePage
from test_frame.page.main import Main


class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["ensureWebviewsHavePages"] = True
            caps["noReset"] = "true"
            # caps["settings[waitForIdleTimeout]"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(8)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def goto_main(self):
        return Main(self.driver)