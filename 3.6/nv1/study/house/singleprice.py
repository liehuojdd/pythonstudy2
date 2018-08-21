
'''
1/3/2018
Send t parameter by url, just change first two letters, ex:
5E9AF59D2467
# http://www.tjfdc.com.cn/Pages/fcdt/HouseInfo.aspx?t=7D4E9AF59D2467&loupan=经纬城市绿洲武清二期&projectname=学知华庭31号楼

Error:UnicodeEncodeError: 'gbk' codec can't encode character '\xa0'
change from
f1.write(myNote.encode('gbk'))
to
f1.write(myNote.encode('gbk','ignore'))
or
str2.replace(u'\xa0', u'')

Error:python write() argument must be str, not bytes
change from
open("temp.txt", "a")
to
open("temp.txt", "wb+")  or ab+
'''
from splinter.browser import Browser
from bs4 import BeautifulSoup
import time
import os

class singleprice:

    fileName='single.csv'

    chromeDriverpath = 'C:\Program Files\Java\webdriver\chromedriver.exe'  # Web driver path
    executable_path = {'executable_path': chromeDriverpath}  # DO NOT change it
    browser = Browser('chrome', **executable_path)  # DO NOT change it

    def __init__(self):
        #self.browser.visit(self.url)
        a=1

    def getinfo(self,url):
        time.sleep(2)
        try:
            self.browser.visit(url)

            innerhtml = self.browser.html
            soup = BeautifulSoup(innerhtml, "lxml")
            soup.replaceWith
            strTotal = ''
            for elem in soup.find_all('td'):
                str1 = elem.text
                str2 = str1.replace('\n', '')  # remove \n
                str3 = str2.strip()  # remove space
                strTotal = strTotal + str3 + ','
            strTotal = strTotal + '\n'
            self.writeLog(strTotal)
        except Exception:
            None

    def writeLog(self,myNote):
        #time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        f1 = open(self.fileName, 'ab+')
        #f1.write(str(myNote))
        #f1.write(str(myNote).encode('utf-8'))
        #string.replace(u’\xa0’, u’ ‘)
        f1.write(str(myNote).encode('gbk','ignore'))
        f1.write(str(myNote).encode('gbk', 'ignore'))
        f1.close()

    def getByCode(self,urlStart,urlEnd):
        url=''
        # Number+Letter
        # Range from 0 to 9
        for i in range(0,10):
            url=str(i)
            for j in range(65, 91):
                print("getting id "+str(i)+chr(j))
                url=urlStart+str(i)+chr(j)+urlEnd
                self.getinfo(url)
        # Letter+Number
        for i in range(65, 91):
            url=str(i)
            for j in range(0, 10):
                print("getting id "+chr(i)+str(j))
                url=urlStart+chr(i)+str(j)+urlEnd
                self.getinfo(url)

        # Letter+Letter
        for i in range(65, 91):
            url=str(i)
            for j in range(65, 91):
                print("getting id "+chr(i)+chr(j))
                url=urlStart+chr(i)+chr(j)+urlEnd
                self.getinfo(url)

        # Number+Number
        for i in range(0, 10):
            url = str(i)
            for j in range(0, 10):
                print("getting id " + str(i) + str(j))
                url = urlStart + str(i) + str(j) + urlEnd
                self.getinfo(url)






