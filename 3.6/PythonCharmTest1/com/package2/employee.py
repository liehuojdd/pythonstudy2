class employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount+=1

    def displayCount(self):
        print("Total employ %d"%employee.empCount)

    def displayEmployee(self):
        print("Name is %s"%self.name)

    def __del__(self):
        print("object distoried ",self.__class__.__name__)
        pass

