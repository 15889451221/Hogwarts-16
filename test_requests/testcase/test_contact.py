import pytest
from jsonpath import jsonpath

from test_requests.req_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = "hello1234"
        self.name = "hello_wolrd"

    @pytest.mark.parametrize("corpid,corpsecret,result",[(None,None,0),("xxx",None,40013),(None,"xxx",40001)])
    def test_token(self,corpid,corpsecret,result):
        r = self.contact.get_token(corpid,corpsecret)
        assert r.get("errcode")==result
        print(r)

    def test_create(self):
        self.contact.create_member(userid=self.userid,name=self.name,mobile="13800000002",department=[1],alias="xxx")
        try:
            find_result = self.contact.find_member(userid=self.userid)
        finally:
            r = self.contact.delete_member(self.userid)
        assert find_result["name"] == self.name

    def test_update(self):
        change_mobile="13800000003"
        self.contact.create_member(userid=self.userid,name=self.name,mobile="13800000002",department=[1],alias="xxx")
        self.contact.update_member(userid=self.userid, name=self.name, mobile=change_mobile)
        try:
            result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert result["mobile"] ==change_mobile


    # @pytest.mark.parametrize("rep",(range(0,20)))
    def test_find_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="13800000002", department=[1],alias="xxx")
        try:
            result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(userid=self.userid)
        assert result["name"]==self.name

    def test_delete(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="13800000002", department=[1],alias="xxx")
        try:
            result = self.contact.find_member(self.userid)
        finally:
            r = self.contact.delete_member(self.userid)
        assert result["userid"]==self.userid



