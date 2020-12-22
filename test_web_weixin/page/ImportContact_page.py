from selenium.webdriver.common.by import By

from test_web_weixin.page.Base_page import BasePage


class ImportContact(BasePage):
    def back_Contact(self):
        pass

    def get_title(self):
        return self.find(By.CSS_SELECTOR,".ww_normalCntHead_title").text