

class TXT(object):
    def __init__(self, filepath):
        self._filepath = filepath

    def read(self):
        return open(self._filepath)
