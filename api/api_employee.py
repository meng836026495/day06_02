import requests
import api


class ApiEmployee():
    # 初始化
    def __init__(self):
        # 新增员工url
        self.url_add = api.BASE_URL + '/api/sys/user'
        self.url_del = api.BASE_URL + '/api/sys/user/{}'
        # 修改员工url
        self.url_put = api.BASE_URL + '/api/sys/user/{}'
        # 查询员工url
        self.url_get = api.BASE_URL + '/api/sys/user/{}'

    # 新增员工
    def user_post(self,username,mobile,workNumber):
        # 定义data数据
        data = {"username":username,"mobile":mobile,"workNumber":workNumber}
        # 调用post方法
        return requests.post(self.url_add,json=data,headers=api.headers)
    # 修改员工
    def user_put(self,username,id):
        # 定义修改的data数据
        data = {"username":username}
        # 调用put方法
        return requests.put(self.url_put.format(id),json=data,headers=api.headers)


    # 查询员工
    def user_get(self,id):
        # 调用get方法
        return requests.get(self.url_get.format(id),headers=api.headers)




    # 删除员工
    def user_delete(self,id):
        # 调用delete方法
        return requests.delete(self.url_del.format(id),headers=api.headers)