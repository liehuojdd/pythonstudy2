import time

a=time.strftime("%Y%m%d%H%M%S%MS", time.localtime())
print(a)
"""
Compare the date str and now
"""
##timeA="5 28 22:24:24 2016"
timeA="8 10 14:30:00 2016"
timeATick=time.mktime(time.strptime(timeA,"%m %d %H:%M:%S %Y"))
print(timeATick)
print(time.time())
if timeATick<time.time():
    print("The date before now")
else:
    print("The date after now")