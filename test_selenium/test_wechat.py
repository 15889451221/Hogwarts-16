import os
from time import sleep

import pytest
import yaml
from selenium import webdriver


class Testwechat():
    '''
    @pytest.mark.skip
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
    @pytest.mark.skip
    def test_cookies(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/")
        cookies=[{'domain': '.qq.com', 'expiry': 1608311788, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850920942787'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 's4SHBEhF9xpzWQnMIv4RUTToaSR-srQlWbTci8sya7rTSHukLawuaG_LqPqw32-weg2Ksbgvrs22Cd9M514u2AEoXytGtVR0yxTe95XRu9HlTUXPTIEOyGXjmNRCUPGoSTPeXYiSEFtGroSo7I_W8sqqKBDU3SYv2gkh0CZb2wbilHHIEPDcPsBaXc2qLV4a8etBBtVCzDjIs7KAl-gJlCAd6vt8-GSlnVuM-FVUqFDsKqm4ZWkBukJPqNFgkPK6p1ffZbEXVn9AOXvYzAbiNQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850920942787'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325112205887'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9862487'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608342727, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3i0ab4a'}, {'domain': '.qq.com', 'expiry': 1608398035, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1533948952.1608311192'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1915721589390656'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '4WeqJLUHx3ew88Sb_ZqTV5ycWjSXhBR94F617Aq0D2I_UynazdU4Ml9AoVUk2zmR'}, {'domain': '.qq.com', 'expiry': 1671383635, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1925473671.1608311192'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639847191, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610903731, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
        self.driver.quit()
    '''
    @pytest.fixture()
    def fixture(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        yield
        self.driver.quit()

    def find_id(self,ele):
        id = self.driver.find_element_by_id(ele)
        return id
    def find_link(self,ele):
        link = self.driver.find_element_by_link_text(ele)
        return link
    def find_xpath(self,ele):
        xpath = self.driver.find_element_by_xpath(ele)
        return xpath


    def test_getcookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = self.driver.get_cookies()
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    @pytest.mark.parametrize("name,child,account,phone,lead", [("夏目", "xiaoxia", "xxx", "15889451223", "负责人"),
                                                               ("夏目1", "xiaoxia1", "xxx1", "15889451224", "负责人1")])
    def test_login(self,name,child,account,phone,lead,fixture):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("data.yaml",encoding="UTF-8")as f:
            yaml_data=yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_link_text("添加成员").click()
        self.find_id("username").send_keys(name)
        self.find_id("memberAdd_english_name").send_keys(child)
        self.find_id("memberAdd_acctid").send_keys(account)
        self.find_id("memberAdd_phone").send_keys(phone)
        self.find_id("memberAdd_title").send_keys(lead)
        self.find_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()
        sleep(3)
        ele = self.find_xpath("//*[@id='member_list']/tr[2]/td[5]/span").text
        print(ele)
        assert ele==phone,"验证结果错误"

    