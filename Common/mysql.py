# coding:utf-8


import pymysql
from Common.readConfig import Config

class MysqlHelper():

    def __init__(self, host, port, db, user, password):
        # 链接数据库
        self.db = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
        # 创建游标
        self.cursor = self.db.cursor()

    def get_data(self, sql):
        '''获取数据'''
        # 执行sql
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res


if __name__ == '__main__':
    host = Config().config_get("DATABASES", "host")
    port = int(Config().config_get("DATABASES", "port"))
    db = Config().config_get("DATABASES", "db")
    user = Config().config_get("DATABASES", "user")
    password = Config().config_get("DATABASES", "password")

    sql = "select * from sales_s_loanuser t where t.IDCARD = '320124198607032218'"

    mysql_helper = MysqlHelper(host, port, db, user, password)
    print(mysql_helper.get_data(sql))





