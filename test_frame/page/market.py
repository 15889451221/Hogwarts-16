from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage
from test_frame.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find_and_click(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        return Search(self.driver)
