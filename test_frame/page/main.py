import yaml
from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.market import Market
from test_frame.page.pre_page import PrePage


class Main(PrePage):

    def goto_market(self):
        # self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH,'//*[@resource-id="android:id/tabs"]//*[@text="行情"]')
        self.basepage.load("../page/main.yaml")

        return Market(self.basepage)