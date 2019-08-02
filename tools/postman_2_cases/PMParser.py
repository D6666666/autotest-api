import json
from logging import Logger

from common.log import Log

logger = Logger('test')


class BaseDataSource(object):
    def __init__(self):
        pass

    def populate(self):
        raise NotImplementedError


class PMDataSource(BaseDataSource):
    def __init__(self, mindex, cindex):
        super(PMDataSource, self).__init__()
        self._mindex = mindex
        self._cindex = cindex
        '''
        self._modular_cnt = 0
        self._case_cnt = 0
        self.title = None
        self._modular_list = []
        # self._single_case_list = []
        self._case_list = []
        '''

    def populate(self):
        with open('./test.json', encoding='utf-8') as pmdata:
            jdata = json.load(pmdata)
            '''
            pmp = PMParser(jdata)
            self.title = pmp.title
            self._modular_cnt = len(pmp.modulars)
            for _mindex in range(self._modular_cnt):
                mdp = ModularParser(jdata, _mindex)
                self._modular_list.append(mdp.modular)
                self._case_cnt = len(mdp.cases)
                for _cindex in range(self._case_cnt):
            '''
        return CasesParser(jdata, self._mindex, self._cindex)


class PMParser(object):
    def __init__(self, json_dict):
        self._title = json_dict['info']['name']
        self._modulars = json_dict['item']

    @property
    def title(self):
        """
        get case name
        :return:  casename
        """
        assert self._title is not None
        return self._title

    @property
    def modulars(self):
        """
        get case name
        :return:  casename
        """
        assert self._modulars is not None
        return self._modulars


'''
if '_postman_isSubFolder' in str(self._modulars[mindex]):
    self._modular = self._modulars[mindex]['item'][0]['name']
    self._cases = self._modulars[mindex]['item'][0]['item']
else:
'''


class ModularParser(PMParser):
    def __init__(self, json_dict, mindex):
        super(ModularParser, self).__init__(json_dict)
        try:
            self._modular = self._modulars[mindex]['name']
            self._cases = self._modulars[mindex]['item']
        except IndexError as e:
            logger.error('ModularParser index {}, {}'.format(mindex, e))
            self._modular = None
            self._cases = None

    @property
    def modular(self):
        """
        get uuid
        :return: uuid
        """
        return self._modular

    @property
    def cases(self):
        """
        get uuid
        :return: uuid
        """
        return self._cases


class CasesParser(ModularParser):
    def __init__(self, json_dict, mindex, cindex):
        super(CasesParser, self).__init__(json_dict, mindex)
        try:
            # casename
            self._casename = self.cases[cindex]['name']
            # mode
            self._mode = self.cases[cindex]['request']['method']
            # params
            self._uuid = (self.cases[cindex]['request']['url']['raw'].split('uuid=')[1].split('&')[0] if 'uuid=' in str(self.cases[cindex]['request']['url']) else 'NA')
            self._did = (self.cases[cindex]['request']['url']['raw'].split('did=')[1].split('&')[0] if 'did=' in str(self.cases[cindex]['request']['url']) else 'NA')
            self._pageNum = (self.cases[cindex]['request']['url']['raw'].split('pageNum=')[1].split('&')[0] if 'pageNum=' in str(self.cases[cindex]['request']['url']) else 'NA')
            self._key = (self.cases[cindex]['request']['url']['raw'].split('key=')[1].split('&')[0] if 'key=' in str(self.cases[cindex]['request']['url']) else 'NA')
            self._index = (self.cases[cindex]['request']['url']['raw'].split('index=')[1].split('&')[0] if 'index=' in str(self.cases[cindex]['request']['url']) else 'NA')
            self._company = (self.cases[cindex]['request']['url']['raw'].split('company=')[1].split('&')[0] if 'company=' in str(self.cases[cindex]['request']['url']) else 'NA')
            # path
            self._path = (None if 'path' not in self.cases[cindex]['request']['url'] else ''.join(['/%s' % _p for _p in self.cases[cindex]['request']['url']['path']]))
            # body
            self._body_data = (self.cases[cindex]['request']['body']['raw'] if self._mode == 'POST' and 'raw' in str(self.cases[cindex]['request']['body']) else 'NA')
            self._expect = None
        except (IndexError, TypeError) as ie:
            logger.error('CasesParser index {}, {}'.format(cindex, ie))
            self._casename = None
            self._mode = None
            self._uuid = None
            self._did = None
            self._pageNum = None
            self._key = None
            self._index = None
            self._company = None
            self._path = None
            self._body_data = None
            self._expect = None

    @property
    def casename(self):
        """
        get uuid
        :return: uuid
        """
        return self._casename

    @property
    def body_data(self):
        """
        get uuid
        :return: uuid
        """
        return self._body_data

    @property
    def uuid(self):
        """
        get uuid
        :return: uuid
        """
        return self._uuid

    @property
    def did(self):
        """
        get did
        :return: did
        """
        return self._did

    @property
    def pageNum(self):
        """
        get pageNum
        :return: pageNum
        """
        return self._pageNum

    @property
    def key(self):
        """
        get key
        :return: key
        """
        return self._key

    @property
    def index(self):
        """
        get index
        :return: index
        """
        return self._index

    @property
    def company(self):
        """
        get company
        :return: company
        """
        return self._company

    @property
    def path(self):
        """
        get path
        :return: path
        """
        return self._path

    @property
    def mode(self):
        """
        get mode
        :return: mode
        """
        return self._mode

    @property
    def expect(self):
        """
        get expect
        :return: expect
        """
        return self._expect
