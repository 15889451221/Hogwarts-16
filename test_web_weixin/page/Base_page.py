from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,base_driver=None):
        base_driver : WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.add_cookie_login()
            self.driver.maximize_window()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def add_cookie_login(self):
        with open("../testcases/data.yaml") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self,by,value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by = by,value= value)

    def finds(self,by,value=None):
        if value is None:
            return self.driver.find_elements(*by)
        else:
            return  self.driver.find_elements(by=by,value=value)


    def wait_click(self,locator):
        return WebDriverWait(self.driver,9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.quit()




