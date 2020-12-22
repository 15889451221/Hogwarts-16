from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from test_web_weixin.page.AddDeportment_page import AddDeportment
from test_web_weixin.page.Base_page import BasePage
from test_web_weixin.page.ImportContact_page import ImportContact


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    def goto_add_member(self):
        from test_web_weixin.page.AddMember_page import AddMember

        # WebDriverWait(self.driver,10).until(
        #     expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".ww_operationBar .js_add_member")))
        self.wait_click(self._location_goto_add_member)

        self.find(self._location_goto_add_member).click()
        return AddMember(self.driver)

    def get_member(self):
        member_list = self.finds(*self._location_member_list)
        # 列表推导式
        member_list_res = [i.text for i in member_list]
        return member_list_res

    # 定位有误
    def goto_import_contact(self):
        self.wait_click((By.XPATH,'//*[@id="js_contacts234"]/div/div[2]/div/div[2]/div[3]/div[9]/div[2]/a/div[2]/span'))
        self.find(By.XPATH,'//*[@id="js_contacts234"]/div/div[2]/div/div[2]/div[3]/div[9]/div[2]/a/div[2]/span').click()
        sleep(3)
        self.find(By.XPATH,"//*[@id='js_contacts234']/div/div[2]/div/div[2]/div[3]/div[9]/div[2]/div/ul/li[1]/a/text()").click()
        return ImportContact(self.driver)

    def goto_add_deportment(self):
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.find(By.XPATH,"//*[@id='js_contacts173']/div/div[1]/ul/li[1]/a").click()
        self.find(By.XPATH,"//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[1]/input").send_keys("研发部")
        self.driver.find_element(By.CSS_SELECTOR, ".js_toggle_party_list span.ww_btn_Dropdown_arrow").click()
        self.driver.find_elements_by_xpath('//form//a[@class="jstree-anchor"]')[1].click()
        self.driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn ww_btn_Blue']").click()
        return AddDeportment(self.driver)
