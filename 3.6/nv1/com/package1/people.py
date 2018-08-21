class people:
    name='jack'
    __age=12
    country='China'

    def __init__(self):#Constructor
        print("Constructor")

    def printName(self):#Function
        print(self.name)

    def function2(anyothers):#Not only can self, you can use others name
        print(anyothers.country)

    @staticmethod
    def getCountry():#Static method
        return people.country