
from splinter.browser import Browser
from bs4 import BeautifulSoup
import time
import os

class house:
    urlSearchContract='http://www.tjfdc.com.cn/pages/fcdt/SpfConSearch.aspx?selmnu=FCSJ_ZXCX_SPF&type=1'
    #urlSearchContract='http://localhost:8082/test/hoursesearch.html'
    urlLouDong='http://www.tjfdc.com.cn/Pages/fcdt/LouDongList.aspx?selmnu=FCSJ_XMXX_LPB&fid='
    # &XMMC=经纬城市绿洲武清二期&PTYPE
    urlSearchProject='http://www.tjfdc.com.cn/Pages/fcdt/fcdtlist.aspx?SelMnu=FCSJ_XMXX&KPZT=&strKPZT=&QY=&XZQH=&strXZQH=&BK=&XMMC='+\
                     '%E7%BB%8F%E7%BA%AC%E5%9F%8E%E5%B8%82%E7%BB%BF%E6%B4%B2%E6%AD%A6%E6%B8%85%E4%BA%8C%E6%9C%9F&PTYPE=&e=0.628716823921011'
    idCard=''
    paperNumber=''
    fileName='searchInfo.txt'

    chromeDriverpath = 'C:\Program Files\Java\webdriver\chromedriver.exe'  # Web driver path
    executable_path = {'executable_path': chromeDriverpath}  # DO NOT change it
    browser = Browser('chrome', **executable_path)  # DO NOT change it
    '''
    send json here, need yzm
    http://www.tjfdc.com.cn/pages/fcdt/data/SearchHandler.ashx?Cols=Costomer,Use,Contractno,Houseaddr,Begindate,Enddate,Savedate,Firstdate,Dj_date,Dy_sj,Qfdysj,Seconddate,Lastdate,Csdjsj,Scmj,
    URL,SRC&stype=%E4%B9%B0%E6%96%B9%E8%AF%81%E4%BB%B6%E5%8F%B7&zjhm1=2201234&zjhm2=2017-5678&type=2&yzm=3194&e=0.6934480364488461
    '''

    def __init__(self):
        self.browser.visit(self.urlSearchContract)
        #self.browser.visit(self.urlSearchProject)

    def search(self):
        self.browser.fill('txtZjmc1',self.idCard)
        self.browser.fill('txtZjmc2', self.paperNumber)
        searchBtn = self.browser.find_by_id('divBt')
        #time.sleep(4)
        #searchBtn.click()
        print('Press enter to continue, or prss r to retry.')
        letter=input()
        if letter=='r':
            self.search()
        else:
            return

    def openanother(self):
        self.browser.visit(self.urlSearchProject)

    def getinfo(self):
        innerhtml=self.browser.html
        soup=BeautifulSoup(innerhtml,"lxml")
        elem1=soup.find(attrs={'id':'divListSpf'})
        strTotal = ''
        for elem in elem1.find_all('td'):
            str1 = elem.text
            str2=str1.strip()
            strTotal=strTotal+str2+','
        strTotal = strTotal + '\n'
        self.writeLog(strTotal)
        self.browser.quit()

    def writeLog(self,myNote):
        time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        f1 = open(self.fileName, 'ab+')
        str1=time1+'\n'+myNote
        f1.write(str1.encode('utf-8'))
        f1.close()

    # Get the lou dong list
    def louDong(self):
        url=self.urlLouDong+self.getFid()
        self.browser.visit(url)
        innerhtml = self.browser.html
        soup1 = BeautifulSoup(innerhtml,"lxml")
        elem1 = soup1.find(attrs={'id': 'divLouDongList'})
        i=0
        for line in elem1.find_all('tr'):
            a=str(line)+'\n'
            i=i+1
            if i==4:
                return;

    def getFid(self):
        innerhtml = self.browser.html
        soup1 = BeautifulSoup(innerhtml,"lxml")
        elem1 = soup1.find(attrs={'class': 'picl_tit fl blue01'})
        linkHref=elem1['href']
        strFind = 'fid='
        strNow = linkHref[linkHref.find(strFind) + len(strFind):]
        return strNow
    def main(self):
        self.search()
        #self.getinfo()
        self.openanother()




