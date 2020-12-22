import yaml
from selenium import webdriver


class TestWechart:
    def test_getcookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = self.driver.get_cookies()
        with open("../testcases/data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)