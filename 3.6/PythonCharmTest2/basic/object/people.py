'''
The more comments
Line2
'''
class people:
    name='jack'
    __age=12
    birth=''
    sex=''

    def __init__(self,name):
        self.name=name
        print('constructor')

    def __functionA(self):
        pass

    @staticmethod
    def getStaticCountry():
        return 'TianJin'

    def noSelf(seName):
        return seName

    @birth.setter
    def birthfun(self,value):
        self.birth=value

    @property
    def sexfun(self,value):
        self.sex=value