from xlrd import open_workbook
from xlutils.copy import copy


class Excel(object):
    def __init__(self, file_path):
        self.path = file_path

    def w(self, content):
        rexcel = open_workbook(self.path)  # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
        excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
        row = rows
        for i in range(len(content)):
            print(content)
            table.write(row, i, content[i])  # xlwt对象的写方法，参数分别是行、列、值
        excel.save(self.path)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel

