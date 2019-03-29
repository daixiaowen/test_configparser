# coding:utf-8

import requests, json
from Common.log import log1

class webrequests():
    def get(self, url, params=None, headers=None, files=None):
        '''封装get方法，返回状态码和响应内容'''
        try:
            response = requests.get(url, params=params, headers=headers, files=files)
            log1.info("请求的参数是:{}".format(params))
            response_statu_code = response.status_code
            log1.info("返回的状态码是:{}".format(response_statu_code))
            response_text = response.content.decode('utf-8')
            log1.info("响应内容是:{}".format(response_text))
        except BaseException as e:
            log1.error("请求错误:{}".format(e))


    def post(self, url, params=None, headers=None, files=None):
        '''封装post请求'''
        try:
            response = requests.post(url, params=params, headers=headers, files=files)
            log1.info("请求url:{}".format(url))
            log1.info("请求参数:{}".format(params))
            log1.info("响应状态码:{}".format(response.status_code))
            log1.info("响应内容:{}".format(response.text))
            return response
        except BaseException as e:
            log1.error("请求错误:{}".format(e))

    def post_json(self, url, params=None, headers=None, files=None):
        '''封装请求参数为json格式的post请求'''
        try:
            json_params = json.dumps(params)
            response = requests.post(url, params=json_params, headers=headers, files=files)
            log1.info("请求url:{}".format(url))
            log1.info("请求参数:{}".format(params))
            log1.info("响应状态码:{}".format(response.status_code))
            log1.info("响应内容:{}".format(response.text))
            return response
        except BaseException as e:
            log1.error("请求错误:{}".format(e))


