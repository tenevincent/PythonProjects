
class person:
    def __init__(self, name):
        self.__name=name
    def setname(self, name):
        self.__name=name
        self.__initialize()
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name
    def __initialize(self):
        print('setname() called')        
        print('initialize() called') 
    name=property(getname, setname, delname)