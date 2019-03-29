# coding:utf-8

# import smtplib
# from Common.readConfig import Config
# from email.mime.text import MIMEText  # 发送纯文本邮件
# from email.header import Header
#
# sender = "924925678@qq.com"  # 发件人邮箱
# password = "hpwhiqdjfgmabebf"  # 发件人邮箱密码
# address_email = ("924925678@qq.com", "232975718@qq.com")  # 收件人邮箱
#
# def send_email():
#     try:
#         # 构造邮件
#         message = MIMEText("这是邮件主体", 'plain', 'utf-8')
#         message["From"] = Header("随风", 'utf-8')
#         message['To'] = Header('a, b , c', "utf-8")
#         message["Subject"] = Header("这是标题", "utf-8")
#
#         # 发送邮件
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)
#         server.login(sender, password)  #　登录
#         server.sendmail(sender, address_email, message.as_string())
#         server.quit()
#     except Exception:
#         print("邮件发送失败")
# send_email()


import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

t = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

def send_email(sender, password, address_email, file):
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = formataddr(["发件人姓名", sender])
        message["To"] = formataddr(["收件人姓名", address_email])
        message["Subject"] = "测试发送邮件"  # 发送邮件标题

        # 邮件正文内容
        message.attach(MIMEText("这是邮件主体内容", "plain", "utf-8"))

        # 构造附件
        # att1 = MIMEText(open(run_all.report_real_path, 'rb').read(), "plain", "utf-8")
        #
        # att1["Content-Type"] = 'application/octet-stream'
        # # filename是附件名，附件名称为中文时的写法
        # att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试.txt"))
        # message.attach(att1)

        # 构造附件2
        att2 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        #附件名称非中文时的写法
        att2["Content-Disposition"] = 'attachment; filename="report.html"'
        message.attach(att2)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，一般端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, address_email.split(","), message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接

    except Exception:
        print("发送邮件失败！")

