#coding=utf-8
#作者：cq
#创建时间：2019/5/17 14:25
#IDE: PyCharm


class FormatTrans(object):
    def __init__(self, data):
        self._data = data
        # casename
        self._casename = str(self._data["casename"])
        # mode
        self._mode = self._data['mode']
        # path
        self._path = self._data['path']
        # token
        # self._token = self._data['token']
        # params
        self._plateNumOrParkingName = self._data['plateNumOrParkingName']
        self._parkingId = self._data['parkingId']
        #self._pageNum = self._data['pageNum']
        self._carId = self._data['carId']
        self._destined = self._data['destined']
        # body
        self._body = self._data['body_data'].encode('utf-8') if self._data['body_data'] != 'NA' and self._data['body_data'] is not None else ''
        # expected
        self._expect = self._data['expect']
        # skip
        self._skip = self._data['skip_tag']
        # params 2 json
        self._parame = {}
        if self._plateNumOrParkingName != 'NA':
            self._parame['plateNumOrParkingName'] = '' if self._plateNumOrParkingName is None else self._plateNumOrParkingName
        if self._parkingId != 'NA':
            self._parame['parkingId'] = '' if self._parkingId is None else self._parkingId
        # if self._pageNum != 'NA':
        #     self._parame['pageNum'] = '' if self._pageNum is None else self._pageNum
        if self._carId != 'NA':
            self._parame['carId'] = '' if self._carId is None else self._carId
        if self._destined != 'NA':
            self._parame['destined'] = '' if self._destined is None else self._destined

    @property
    def casename(self):
        """
        get casename
        :return: casename
        """
        return self._casename

    @property
    def mode(self):
        """
        get mode
        :return: mode
        """
        return self._mode


    @property
    def path(self):
        """
        get path
        :return: path
        """
        return self._path

    @property
    def parame(self):
        """
        get parame
        :return: parame
        """
        return self._parame

    @property
    def body(self):
        """
        get body
        :return: body
        """
        return self._body

    @property
    def expect(self):
        """
        get body
        :return: body
        """
        return self._expect

    @property
    def skip(self):
        """
        get skip
        :return: skip
        """
        return self._skip
