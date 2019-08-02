# @Author  : 程前

import requests
import readConfig
from .log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        #global host, timeout
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        #self.headers = {"Content-Type": "application/json"}

        # if type == "con":
        #     self.headers = localReadConfig.get_con("headers")
        #     host = localReadConfig.get_con("url")
        #     timeout = localReadConfig.get_con("timeout")
        # elif type == "pre":
        #     self.headers = localReadConfig.get_con("headers")
        #     host = localReadConfig.get_pre("url")
        #     timeout = localReadConfig.get_pre("timeout")
        # else:
        #     self.logger.error("Interface Type ERROR!")

    # def set_url(self, url):
    #     self.url = host + url
    #
    # def set_headers(self, header):
    #     self.headers = header
    #
    # def set_params(self, param):
    #     self.params = param
    #
    # def set_data(self, data):
    #     self.data = data

    # defined http get method
    def get(self,url,timeout, params=None,headers=None):
        try:
            response = requests.get(url, params=params,headers=headers,timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
        except Exception as e:
            self.logger.error('请求出错,出错原因:{}. url: {}. params: {}'.format(e, url, params))
            return None

    # defined http post method
    def post(self,url,params,timeout,headers=None):
        try:
            response = requests.post(url,data=params, headers=headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
        except Exception as e:
            self.logger.error('请求出错,出错原因:{}. url: {}. params: {}'.format(e, url, params))
            return None


# if __name__ == "__main__":
#     print("ConfigHTTP")