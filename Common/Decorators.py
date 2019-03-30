# coding:utf-8

import time
from Common.log import log1

def decorators(f):
    def wrapper(*args, **kwargs):
        log1.info("请求参数：{}".format(args, kwargs))
        print(time.ctime())
        return f(*args, **kwargs)
    return wrapper