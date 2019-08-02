# @Author  : 程前


import os
import codecs
import configparser

#proDir = os.path.split(os.path.realpath("__file__"))[0]
proDir = os.path.split(__file__)[0]
configPath = os.path.join(proDir,"config","config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:4] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_test(self, name):
        value = self.cf.get("159", name)
        return value

    def get_pre(self, name):
        value = self.cf.get("PER", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value