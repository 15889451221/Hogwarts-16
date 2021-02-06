import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = "wwceee941baa19cab7"
        self.corpsecret = "PxlKHlaiBLIQEs3jzJZCoBrbHQu4geUvtqso_4WCBbw"
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self,corpid=None,corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {'corpid':corpid,'corpsecret':corpsecret}
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        # assert 0 == r.json()["errcode"]
        # token = r.json()["access_token"]
        return r.json()