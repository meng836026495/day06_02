import unittest

from api.api_login import ApiLogin
from tools.assert_common import duanyan
from api import headers

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_login = ApiLogin()


    def test01_login(self,mobile="13800000002",passsword="123456"):
        r = self.api_login.login(mobile,passsword)
        duanyan(self,r)
        token = r.json().get("data")
        headers["Authorization"]="Bearer "+token
        print(headers)
        print(r.json())
        print(r.status_code)




