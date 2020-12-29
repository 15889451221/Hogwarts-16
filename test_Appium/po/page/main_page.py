from appium.webdriver.common.mobileby import MobileBy

from test_Appium.po.page.address_list_page import AddressListPage
from test_Appium.po.page.base_page import BasePage


class MainPage(BasePage):
    def goto_address(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")

        return AddressListPage(self.driver)