from time import sleep

from selenium.webdriver.common.by import By

from test_web_weixin.page.Base_page import BasePage


class AddDeportment(BasePage):
    def goto_import_contact(self):
        pass
    def get_title(self):
        # self.driver.switch_to.frame("frame_cnt frame_cnt_SuperAdmin")
        # self.find(By.CSS_SELECTOR,".jstree-closed .jstree-ocl").click()
        # self.find(By.ID,"1688850920944335_anchor").click()
        sleep(5)
        res= self.find(By.CSS_SELECTOR,'.jstree-clicked').text
        # a = self.driver.find_element_by_css_selector(".ww_commonCntHead_NoBorder .ww_commonCntHead_title_inner_text").text
        print(res)
        return res

    def goto_add_member(self):
        pass