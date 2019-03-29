# coding:utf-8

import configparser, xlrd

class Operate_Excel(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file = r"D:\test_configparser\Config\config.ini"
        self.config.read(self.file)

    def test_excel(self, excel_path, sheet_name):

        open_excel = xlrd.open_workbook(excel_path)
        # 获取所有sheet名称
        sheet_names = open_excel.sheet_names()
        # 操作sheet_name
        get_sheet = open_excel.sheet_by_name(sheet_name)

        # 将excel的第一行的值，作为keys
        self.keys = get_sheet.row_values(0)

        # 获取sheet_name的总列数和总行数
        self.nrows = get_sheet.nrows
        self.ncols = get_sheet.ncols

        for sheet in sheet_names:
            if sheet == sheet_name:
                if self.nrows <= 1:
                    print("总行数<=1")
                else:
                    new_list = []
                    j = 1
                    for row in range(self.nrows - 1):
                        # 定义一个空字典，将获取到的key，value以字典的形式存入
                        new_dict = {}
                        # 从第二行开始获取值values
                        values = get_sheet.row_values(j)
                        for col in range(self.ncols):
                            new_dict[self.keys[col]] = values[col]
                        new_list.append(new_dict)
                        j += 1
                    return new_list
            else:
                print("sheet is not exist!!!")

