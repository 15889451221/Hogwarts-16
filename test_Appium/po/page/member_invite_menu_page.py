from appium.webdriver.common.mobileby import MobileBy

from test_Appium.po.page.base_page import BasePage
from test_Appium.po.page.contact_add_page import ContactAdd
class MemberInviteMenuPage(BasePage):
    def add_member_menual(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
        return ContactAdd(self.driver)