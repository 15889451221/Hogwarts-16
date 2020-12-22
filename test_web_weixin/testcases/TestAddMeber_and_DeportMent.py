from time import sleep

import pytest

from test_web_weixin.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    # 首页直接点击，进行添加会员
    def test_add_member(self):
        res=self.main.goto_add_member().add_member().get_member()
        assert "赫敏2" in res,"断言有误"

    @pytest.mark.parametrize("accid,phone,expect_res",[("xxx3", "13199998888", "该帐号已被“赫敏2”占有"),
                                                       ("xx2", "13388881235", "该帐号已被“赫敏2”占有")])
    def test_add_member_fail(self,accid,phone,expect_res):
        res = self.main.goto_add_member().add_member_fail(accid,phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        print(res)
        # assert "赫敏2" in res

    def test_goto_ImportPage(self):
        res = self.main.goto_import_contact().get_title()
        assert "批量导入通讯录"==res

    # def test_contact_goto_import(self):
    #     self.main.goto_contact().goto_import_contact()

    #添加部门
    def test_goto_deportment(self):
        deport_name=self.main.goto_contact().goto_add_deportment().get_title()
        assert "研发部"==deport_name

    def teardown(self):
        self.main.quit()