#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wmzhang
#
# Created:     18/09/2016
# Copyright:   (c) wmzhang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time

class timeToStr:
    def __init__(self):
        pass

    def TimeStr(self):
        timeStr=time.strftime("%Y%m%d%H%M%S%MS", time.localtime())
        #print(timeStr)
        return timeStr

    """
    The timeStr formate should be timeA="8 10 14:30:00 2016"
    """
    def TimeBeforeNow(self,timeStr):
        timeATick=time.mktime(time.strptime(timeStr,"%m %d %H:%M:%S %Y"))
        if timeATick<time.time():
            return True
        else:
            return False

    def AllFormatsOutput(self):
        # 鏍煎紡鍖栨垚2016-03-20 11:45:39褰㈠紡
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        # 鏍煎紡鍖栨垚Sat Mar 28 22:24:24 2016褰㈠紡
        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

        # 灏嗘牸寮忓瓧绗︿覆杞崲涓烘椂闂存埑
        a = "Sat Mar 28 22:24:24 2016"
        print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))