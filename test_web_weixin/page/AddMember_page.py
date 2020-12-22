from selenium.webdriver.common.by import By

from test_web_weixin.page.Base_page import BasePage
from test_web_weixin.page.Contact_Page import ContactPage


class AddMember(BasePage):
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")
    _location_save = (By.CSS_SELECTOR, ".js_btn_save")

    def add_member(self):
        self.find(*self._location_username).send_keys("赫敏2")
        self.find(*self._location_acctid).send_keys("020")
        self.find(*self._location_Add_phone).send_keys("13177778882")
        self.find(*self._location_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self,acctid,phone):
        self.find(*self.location_username).send_keys("赫敏2")
        self.find(*self.location_acctid).send_keys(acctid)
        self.find(*self.location_Add_phone).send_keys(phone)
        self.find(*self.location_save).click()

        # error_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # phone_error_message = self.driver.find_element(By.CSS_SELECTOR,".member_edit_item_right.ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
        # error_list = [error_message, phone_error_message]
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [i.text for i in res]
        print(error_list)
        return error_list
