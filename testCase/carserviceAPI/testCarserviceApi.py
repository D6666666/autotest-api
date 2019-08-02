# @Author  : 程前
import time
import unittest, json
from ddt import data, ddt
import readConfig
from common.log import MyLog
from common import public
from common import configHttp
from testCase.BaseCase.testBaseCase import BaseCase

localReadConfig = readConfig.ReadConfig()


@ddt
class carserviceAPI(BaseCase):
    test_data = public.assembleData("carserviceAPI_case.xlsx")

    @classmethod
    def setUpClass(cls):
        cls.cfg_func = 'get_test'    # config方法名
        super(carserviceAPI, cls).setUpClass()

    @data(*test_data)
    def testcarserviceAPI(self, data):
        return self.baseCase(data)


if __name__ == "__main__":
    unittest.main()
