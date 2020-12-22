from selenium.webdriver.common.by import By

from test_web_weixin.page.AddMember_page import AddMember
from test_web_weixin.page.Base_page import BasePage
from test_web_weixin.page.Contact_Page import ContactPage
from test_web_weixin.page.ImportContact_page import ImportContact


class MainPage(BasePage):
    location_goto_member = (By.CSS_SELECTOR,".ww_indexImg_AddMember")
    location_goto_contact = (By.ID,"menu_contacts")
    def goto_add_member(self):
        self.find(self.location_goto_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(self.location_goto_contact).click()
        return ContactPage(self.driver)

    def goto_import_contact(self):
        self.find(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[2]/div/span[2]").click()
        return ImportContact(self.driver)

def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()