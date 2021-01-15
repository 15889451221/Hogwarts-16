import logging

import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_frame.black_handle import black_wrapper


class BasePage():
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    SEND = "send"
    CONTENT = "content"

    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["ensureWebviewsHavePages"] = True
        caps["noReset"] = "true"
        # caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self,by,locator):
        return self.driver.find_element(by,locator)


    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    def find_and_click(self,by,locator):
        self.find(by,locator).click()

    def send(self,by,locator,content):
        return self.find(by,locator).send_keys(content)

    def scroll_find(self,text):
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        f'text("{text}").instance(0));')
    def scroll_find_click(self,text):
        self.scroll_find(text).click()

    def swip_find(self,by,locator):
        self.driver.implicitly_wait(1)
        eles = self.driver.find_elements(by,locator)
        while len(eles)==0:
            self.driver.swipe(0,600,0,400)
            eles=self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swip_find_click(self,by,locator):
        self.swip_find(by,locator).click()


    def send_keys(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by,locator)
            return len(eles) > 0

    def get_toast(self):
        # 通过如下两种方式定位,平时在登录有提示的地方进行获取判断
        self.driver.find_element(MobileBy.XPATH,'//*[@class=android.widget.Toast]').text
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'Clicked popup')]").text

    def load(self,yaml_path):
        with open(yaml_path,encoding="utf-8") as f :
            data = yaml.load(f)
            for step in data:
                xpath_expr = step.get(self.FIND)
                action = step.get(self.ACTION)
                if action == self.FIND_AND_CLICK:
                    self.find_and_click(MobileBy.XPATH, xpath_expr)
                elif action == self.SEND:
                    content = step.get(self.CONTENT)
                    self.send(MobileBy.XPATH,xpath_expr,content)

    def screenshot(self,picture_path):
        self.driver.save_screenshot(picture_path)