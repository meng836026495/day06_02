import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import duanyan


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.api_emp = ApiEmployee()

    # 新增员工
    def test01_user_add(self,username="holiday",mobile="17631000998",workNumber=25015):
        r = self.api_emp.user_post(username,mobile,workNumber)
        api.user_id = r.json().get("data").get("id")
        duanyan(self,r)
        print("新增后的结果为:",r.json())
        print(api.user_id)

    # 查询员工
    def test02_search(self):
        r = self.api_emp.user_get(api.user_id)
        duanyan(self, r)

    # # 修改员工
    def test03_put(self,username='baby'):
        r = self.api_emp.user_put(username,api.user_id)
        duanyan(self,r)
        print('修改后的结果为:',r.json())



    # 删除员工
    def test04_user_del(self):
        r = self.api_emp.user_delete(api.user_id)
        duanyan(self,r)
        print('删除后的结果为:', r.json())