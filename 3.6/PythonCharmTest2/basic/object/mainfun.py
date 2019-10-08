from basic.object.people import people
from basic.object.student import student

if __name__=='__main__':
    #print(people.getStaticCountry())
    myobj=people('jim')
    # Call failed if no people.__init__(self,name)
    #print(myobj.noSelf('here'))
    # TypeError: noSelf() takes 1 positional argument but 2 were given

    mystu=student()
    mystu.getStaticCountry()
    print(mystu.stuFun())
