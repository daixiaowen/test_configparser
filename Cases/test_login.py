# coding:utf-8

import unittest, requests
from Common.base_test import webrequests
from Common.readConfig import Config
from Common.excel import Operate_Excel

class Login(unittest.TestCase):

    def setUp(self):
        self.c = Config()
        self.s = requests.session()
        self.method = webrequests()
        self.excel = Operate_Excel()
        print("执行测试用例")

    def tearDown(self):
        print("执行用例完毕")

    def login(self, url, username, password):
        '''登录接口'''
        payload = {
            "loginName": username,
            "loginPassword": password
        }
        response = self.method.post(url, params=payload)
        return response

    def test_login001(self):
        '''执行用例001'''
        url = self.c.config_get("HTTP", "url")
        path = self.c.config_get("HTTP", "path")
        new_url = url + path

        excel_path = self.c.config_get("EXCEL", "path")
        user = self.excel.test_excel(excel_path, "manage_login")[0]["loginName"]
        password = self.excel.test_excel(excel_path, "manage_login")[0]["loginPassword"]
        login_res = self.login(new_url, user, password)

        self.assertEqual(login_res.status_code, 200)
        self.assertEqual(login_res.json()['status'], str(200), msg="断言失败")

