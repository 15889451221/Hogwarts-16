from appium.webdriver.common.mobileby import MobileBy

from test_Appium.po.page.base_page import BasePage


class ContactAdd(BasePage):
    def add_contact(self):
        self.send_keys(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']","bbbb")
        self.find_and_click(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@text='男']")
        self.wait_for(MobileBy.XPATH,"//*[@text='女']")
        self.find_and_click(MobileBy.XPATH,"//*[@text='女']")
        self.send_keys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']","15889451332")
        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")
        return True
