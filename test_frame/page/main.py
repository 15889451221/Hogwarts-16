from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_and_click(MobileBy.XPATH,'//*[@resource-id="android:id/tabs"]//*[@text="行情"]')
        return Market(self.driver)