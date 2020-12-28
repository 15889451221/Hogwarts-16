import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDw():
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["platformVersion"] = "6.0"
        desire_caps["deviceName"] = "127.0.0.1:7555"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        desire_caps["noReset"] = "true"
        # desire_caps["dontStopAppOnReset"] = "true"
        desire_caps["unicodeKeyboard"] = "true"
        desire_caps["resetKeyboard"]="true"
        desire_caps["skipDeviceInitialization"] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click();
        price=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert price >200
    @pytest.mark.skip
    def test_attribute(self):
        print(self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").is_enabled())

    @pytest.mark.skip
    def test_touchAction(self):
        action=TouchAction(self.driver)
        rect = self.driver.get_window_rect()
        print(rect)
        width = rect["width"]
        height = rect["height"]
        x1=int(width/2)
        ystart = int(height * 4/5)
        yend = int(height * 1/5)
        action.press(x=x1,y=ystart).wait(2000).move_to(x=x1,y=yend).release().perform()
    @pytest.mark.skip
    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click();
        # 显示等待
        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver,6).until(expected_conditions.element_to_be_clickable(locator))
        #lambda 表达式
        WebDriverWait(self.driver,6).until(lambda x : x.find_element(*locator))
        current_price = self.driver.find_element(*locator).text
        print(f"当前的价格是{current_price}")
        assert float(current_price) >200


    @pytest.mark.skip
    def test_info(self):
        """
        1.点击进入我的
        2.点击登录，进入登录页面
        3.输入用户名、密码
        4.点击登录
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        # 组合定位
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")')

    @pytest.mark.skip
    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("诗与星空").instance(0));').click()
        time.sleep(5)

    def test_attribute(self):
        # pass
        # # 获取元素的属性 并且返回
        # el = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # print(el.get_attribute("content-desc"))
        # print(el.get_attribute("resource-id"))
        # print(el.get_attribute("enabled"))
        # print(el.get_attribute("clickable"))
        # print(el.get_attribute("bounds"))
        self.driver.make_gsm_call("15889451221",GsmCallActions.CALL)



