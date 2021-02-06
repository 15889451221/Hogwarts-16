from typing import List

import requests

from test_requests.req_page.base import Base


class Contact(Base):

    def create_member(self,userid:str,name:str,mobile:str,department:List[int],**kwargs):
        create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
        }
        data.update(kwargs)
        r = self.s.post(url=create_member_url,json=data)
        return r.json()
        # assert r.json().get("errmsg",None) == "created"

    def delete_member(self,userid):
        params = {"userid":userid}
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        # proxies = {"https": "//192.168.0.105:8888"}
        r = self.s.get(delete_member_url, params=params)
        return r.json()
        assert r.json()["errmsg"] == "deleted"

    def update_member(self,userid,name,mobile):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        r = self.s.post(url=update_url, json=data)
        return r.json()
        assert r.json()["errmsg"] == "updated"

    def find_member(self,userid):
        params = {"userid":userid}
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.s.get(get_member_url,params=params)
        return r.json()
        # assert r.json()["name"] == "夏目"