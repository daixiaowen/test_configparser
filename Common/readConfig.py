# coding:utf-8

import configparser, os

class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Config/config.ini")

    def f(self):
        with open(self.file, 'w') as configfile:
            self.config.write(configfile)

    def config_write(self, new_section):
        '''写入,修改config.ini文件'''
        self.config.read(self.file)
        if self.config.has_section(new_section):
            print("section {} exist!!!".format(new_section))
        else:
            self.config.add_section(new_section)

    def config_get(self, section, option=None):
        '''读取config.ini文件'''
        self.config.read(self.file)
        if not self.config.has_section(section):
            print("section {} not exist!!".format(section))
        else:
            # if section in self.config.sections():
            pass
        return self.config.get(section, option)

