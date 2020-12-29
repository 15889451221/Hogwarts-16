from appium.webdriver.common.mobileby import MobileBy

from test_Appium.po.page.base_page import BasePage
from test_Appium.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    def click_AddMember(self):
        # self.scroll_find_click("添加成员")
        self.swip_find_click(MobileBy.XPATH,"//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)