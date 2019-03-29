# coding:utf-8

import HTMLTestRunner
import getcwd, os, time, unittest
from Common.Email import send_email

case_path = os.path.join(getcwd.get_cwd(), "Cases")
report_path = os.path.join(getcwd.get_cwd(), "Report")

t = time.strftime("%Y%m%d%H%MS", time.localtime(time.time()))
# 报告存放绝对路径
report_real_path = os.path.join(report_path, "report.html")

def all_case():
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="test*.py", top_level_dir=None)
    return discover

if __name__ == '__main__':
    with open(report_real_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="登录接口", description="测试结果如下：")
        runner.run(all_case())

    time.sleep(3)

    sender = "9"
    password = ""
    address_email = ""
    receivers = ",".join(address_email)

    send_email(sender, password, receivers, report_real_path)

