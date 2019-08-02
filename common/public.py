# @Author  : 程前

import os, requests, json
from openpyxl import load_workbook
import readConfig
from .log import MyLog as Log

proDir = os.path.join(readConfig.proDir, "testFile")
log = Log.get_log()
logger = log.get_logger()

# def get_file():
#     filelist = next(os.walk(proDir))[2]
#     file_path = []
#     for i in filelist:
#         file_path.append(proDir+"\\"+i)
#     return file_path

def get_data(file):
    wb = load_workbook(file)
    ws = wb['Sheet1']
    rows = ws.rows
    case = []
    theme = []
    flag = 0
    for row in rows:
        flag += 1
        line = [cell1.value for cell1 in row]
        if flag == 1:
            theme = line
        else:
            case.append(dict(zip(theme,line)))
    return case

def assembleData(filename):
    proDir_copy = os.path.join(proDir, filename)
    return get_data(proDir_copy)


def login_token(host,default, params):
    sms_path = '/sendSmsCode?phoneNo=**********'
    path = '/login'
    try:
        requests.get("%s%s&%s" % (host,sms_path,default))
        url = "%s%s?%s" % (host,path,default)
        re = requests.post(url,params,headers={'Content-Type': 'application/json'})
        content = re.content.decode('utf-8')
        respones = json.loads(content)
        token = respones['result']['token']
        logger.info("token： %s" % token)
        return token
    except:
        logger.error("token获取失败！")

def show_return_msg(response):
    url = response.url
    msg = response.text
    print("\n请求地址：" + url)
    print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))


