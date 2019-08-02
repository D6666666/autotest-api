from runCASE import localReadConfig
from tools.file_control.excel import Excel
from tools.postman_2_cases.PMParser import PMDataSource


def pm_2_cases():
    mindex = 0
    cindex = 0
    row = 1
    case_info = ['title', 'modular', 'casename', 'mode', 'path', 'uuid', 'did', 'pageNum', 'key', 'index', 'company', 'body_data', 'expect']
    Excel('E:\\PyCharmProjects\\InterfaceTest\\testFile\\pre_test_file.xls').w(case_info)
    while True:
        pm_ds = PMDataSource(mindex, cindex).populate()
        title = pm_ds.title
        modular = pm_ds.modular
        casename = pm_ds.casename
        mode = pm_ds.mode
        path = pm_ds.path
        uuid = pm_ds.uuid
        did = pm_ds.did
        pageNum = pm_ds.pageNum
        key = pm_ds.key
        index = pm_ds.index
        company = pm_ds.company
        body_data = pm_ds.body_data
        expect = pm_ds.expect
        if pm_ds.casename is None:
            mindex += 1
            cindex = 0

        else:
            case_info = [title, modular, casename, mode, path, uuid, did, pageNum, key, index, company, body_data, expect]
            Excel('E:\\PyCharmProjects\\InterfaceTest\\testFile\\pre_test_file.xls').w(case_info)
            cindex += 1
        if pm_ds.modular is None:
            break
        row += 1

pm_2_cases()
