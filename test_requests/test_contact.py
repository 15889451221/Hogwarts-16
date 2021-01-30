import requests


def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwceee941baa19cab7&corpsecret=PxlKHlaiBLIQEs3jzJZCoBrbHQu4geUvtqso_4WCBbw")
    assert 0 == r.json()["errcode"]
    token = r.json()["access_token"]
    return token

def test_defect_member():
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

def test_create_member():
    create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}"
    data = {
            "userid": "zhangsan123",
            "name": "张三hello",
            "alias": "jackzhang",
            "mobile": "+86 13800000000",
            "department": [1]
    }
    r = requests.post(url=create_member_url,json=data)
    print(r.json())
    assert r.json()["errmsg"] == "created"

def test_delete_member():
    delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan123"
    r = requests.get(delete_member_url)
    print(r.json())
    assert r.json()["errmsg"] == "deleted"