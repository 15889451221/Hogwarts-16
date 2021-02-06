import pytest
import requests

class TestContact:
    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwceee941baa19cab7&corpsecret=PxlKHlaiBLIQEs3jzJZCoBrbHQu4geUvtqso_4WCBbw")
        assert 0 == r.json()["errcode"]
        token = r.json()["access_token"]
        return token

    def create_member(self):
        create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}"
        data = {
                "userid": "zhangsan123",
                "name": "张三hello",
                "alias": "jackzhang",
                "mobile": "+86 13800000000",
                "department": [1]
        }
        r = requests.post(url=create_member_url,json=data)
        print(r.json())
        assert r.json().get("errmsg",None) == "created"

    def setup(self):
        self.create_member()

    def test_delete_member(self):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zhangsan123"
        proxies = {"https": "//192.168.0.105:8888"}
        r = requests.get(delete_member_url, proxies=proxies, verify=False)
        print(r.json())
        assert r.json()["errmsg"] == "deleted"

    def teardown(self):
        delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zhangsan123"
        r = requests.get(delete_member_url)
        print(r.json())

def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwceee941baa19cab7&corpsecret=PxlKHlaiBLIQEs3jzJZCoBrbHQu4geUvtqso_4WCBbw")
    assert 0 == r.json()["errcode"]
    token = r.json()["access_token"]
    return token

@pytest.mark.parametrize("par",range(20))
def test_defect_member(par):
    get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=xxx"
    r = requests.get(get_member_url)
    print(r.json())
    assert r.json()["name"] == "夏目"

def test_update_member():
    update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
    "userid": "xxx",
    "name":"夏目",
    "mobile": "13889450000"
    }
    r = requests.post(url=update_url,json=data)
    print(r.json())
    assert r.json()["errmsg"] == "updated"



@pytest.mark.parametrize("left,right",[(2,6),(3,8),(4,5)])
def test_generate(left,right,pre=1):
    '''
    七点法数据生成
    '''
    result =[]
    lefts = [left-pre,left,left+pre]
    rights = [right-pre,right,right+pre]
    mid =(left+right)//2
    result += lefts
    result.append(mid)
    result += rights
    print(set(result))

from itertools import product
def test_prioiduct():
    '''
    笛卡尔积
    '''
    for x,y,z in product(['a','b','c'],['d','e','f'],['m','n']):
        print(x,y,z)