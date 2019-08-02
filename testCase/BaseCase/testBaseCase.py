# @Author  : 程前
import time
import unittest,json
from ddt import data,ddt
import readConfig
from common.log import MyLog
from common import public
from common import configHttp
from dataDriver.FormatTrans import FormatTrans

localReadConfig = readConfig.ReadConfig()


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = MyLog.get_log()
        cls.logger = cls.log.get_logger()
        if not hasattr(cls, 'cfg_func'):
            raise NoConfigerSetError
        _cfg_func = getattr(cls, 'cfg_func')
        # configure
        cls.timeout = cls.cfg(_cfg_func, "timeout")
        cls.cfg_url = cls.cfg(_cfg_func, "url")
        cls.cfg_params_default = cls.cfg(_cfg_func, "params_default")
        cls.token = public.login_token(cls.cfg_url, cls.cfg_params_default,
                                       cls.cfg(_cfg_func, "params_login"))

    def setUp(self):
        pass

    def tearDown(self):
        if self.info is None:
            self.log.build_case_line(self.case_name, '', '')
        else:
            self.log.build_case_line(self.case_name, str(self.info['code']), str(self.info['message']) if 'message' in self.info.keys() else '')

    def description(self):
        """
        test report description
        :return:
        """
        return self.case_name

    @staticmethod
    def cfg(func, *args):
        """
        reflect to get cfg
        :param func:
        :return:
        """
        rc = localReadConfig
        return getattr(rc, func)(*args)

    def baseCase(self, data):
        # data
        data['token'] = self.token
        ft = FormatTrans(data)
        self.info = None
        self.path = ft.path
        self.parame = ft.parame
        self.body = ft.body
        self.mode = ft.mode
        self.case_name = ft.casename
        self.expect = ft.expect
        self.skip = ft.skip
        if self.skip is True:
            return self.skipTest('{} died with SKIP, cos skip_tag is TRUE'.format(self.case_name))
        # url
        self.url = '%s%s%s%s' % (
        self.cfg_url, self.path, '?' + self.cfg_params_default if self.cfg_params_default != 'NA' else '',
        '&' + '&'.join(['%s=%s' % (_k, _v) for _k, _v in self.parame.items()]))
        self.headers = {"Content-Type":"application/json",'token':self.token}
        # log to record requests data
        self.logger.debug(
            '{} requests data. url: {}, body: {}, mode: {}'.format(self.case_name, self.url, self.body, self.mode))
        self.req = configHttp.ConfigHttp()
        if self.mode == 'GET':
            self.return_json = self.req.get(self.url, self.timeout,headers=self.headers)
        elif self.mode == 'POST':
            self.return_json = self.req.post(self.url, self.body,self.timeout,headers=self.headers)
            self.logger.info(self.url)
        else:
            print('invalid  mode!')
            return

        if self.return_json is None:
            self.logger.info('{} died with False, response: None. Pls check http server'.format(self.case_name))
        # log to record response data
        self.logger.debug('{} response data, rcode: {}, rtext: {}'.format(self.case_name, self.return_json.status_code,
                                                                          self.return_json.text))
        self.info = self.return_json.json()
        self.logger.info('{} died with {}, response code: {}, except code {}'.format(self.case_name, self.info[
            'code'] == self.expect, self.info['code'], self.expect))
        self.assertEqual(self.info['code'], self.expect)
        time.sleep(0.5)


class NoConfigerSetError(Exception):
    def __init__(self):
        super().__init__(self)
        self.errorinfo = 'not set configer function!'

    def __str__(self):
        return self.errorinfo


if __name__ == "__main__":
    unittest.main()
