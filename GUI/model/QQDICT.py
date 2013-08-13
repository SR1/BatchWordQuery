import httplib
from enity.QQWordMeaning import QQWordMeaning

    
QQDICT_HOST = r"dict.qq.com"
QQDICT_PATH = r"/dict?q=%s"

class QQDICT:
    def __init__(self):
        pass

    def getMeaning(self,keyword):
        con = httplib.HTTPConnection(QQDICT_HOST,80)
        con.request('GET', self.buildPath(keyword))
        response = con.getresponse().read()
        word = QQWordMeaning(response)
        return word

    def buildPath(self,keyword):
        return QQDICT_PATH % keyword

