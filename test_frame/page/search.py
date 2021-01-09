from appium.webdriver.common.mobileby import MobileBy

from test_frame.base_page import BasePage


class Search(BasePage):
    def search(self):
        self.find(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys("xxxx")
        return True