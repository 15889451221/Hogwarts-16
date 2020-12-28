from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_CompanyWeChat:
    def setup(self):
        desire_caps={}
        desire_caps["platformName"]="android"
        desire_caps["platformVersion"] = "6.0"
        desire_caps["deviceName"]="127.0.0.1:7555"
        desire_caps["appPackage"]="com.tencent.wework"
        desire_caps["appActivity"]=".launch.WwMainActivity"
        # 设置页面空闲状态等待的时间
        desire_caps["settings[waitForIdleTimeout]"]=0

        # 动态刷新
        desire_caps["ensureWebviewsHavePages"]= True
        desire_caps["noReset"]="true"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        print(self.driver.page_source)
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source




