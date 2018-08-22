#coding=utf-8

'''
Note: 12/29/2017
For feisu, can't get the whole page block by the server setting.
Framework:
Python:2.7
Mechanize (Only support Python 2.*)
Beautifulshoup4  (pip install beautifulsoup4)

Class change as following:
Find the content in two place - id='BookText'
Find the next page as - text=u'\u4e0b\u4e00\u9875', tag=u'a'
Chinese to Unicode, tools:http://tool.chinaz.com/tools/unicode.aspx
Update the content replace with function - replaceStr

Error
UnicodeDecodeError: 'ascii' codec can't decode byte 0xb5 in position 0
add
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
from bs4 import BeautifulSoup
import mechanize
import time
import cookielib
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class biqu:

    url = b'f700006ae880854e6079dc12e996d04ae90f744d3dd123214ccc196f100cc88a659c7150e2390700fae6338252bad79e'
    urlEnd = 'bqge98325'#Seperate the page number by url
    fileName='test1.txt'
    sleepTime=1

    expCount = 0  # Exception count
    expTotal=10 # After exception total, break
    pageTotal=0
    browser = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')]

    br = browser.open(url)
    soup = BeautifulSoup(br, "html5lib")

    def __init__(self):
        a=1

    def main(self):
        firstNote = self.soup.find(id='content')
        #firstNote = self.soup.find(attrs={'class':'p'})
        note2 = firstNote.text
        self.replaceStr(note2,'-1-')

        self.getContentWithException()

    def getContentWithException(self):
        while True:
            try:
                self.getContentForNextPage()
                if self.expCount >= self.expTotal:# Exception
                    break
            except Exception:
                time.sleep(3)
                self.expCount = self.expCount+1
                if self.expCount >= self.expTotal:# Exception
                    break
                else:
                    self.getContentWithException()
                print 'Exception at:' + str(self.expCount) + ' times '

    def getContentForNextPage(self):
            # Click next page
            # debug as links
            links=self.browser.links()
            time.sleep(self.sleepTime)
            nextpage = self.browser.find_link(text=u'下一章', tag=u'a')
            request = self.browser.click_link(nextpage)
            response = self.browser.open(request)
            # Get the content
            soup = BeautifulSoup(response, "html5lib")
            othersNote = soup.find(id='content')
            note2=othersNote.text

            # Print current page url
            urlNow = self.browser.geturl()
            urlNow = urlNow[urlNow.find(self.urlEnd) + len(self.urlEnd):]
            self.replaceStr(note2,urlNow)
            self.pageTotal=self.pageTotal+1
            print 'Page total:'+ str(self.pageTotal) + ' of page ' + urlNow

    def replaceStr(self,string,urlNow):
        f1 = open(self.fileName, 'ab+')
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        # remove from beginning
        strFind = '<br/>'
        i=0
        str2 = str(string)

        str1 = u'\u7b2c' + urlNow + u'\u7ae0' + u'\n'
        f1.write(str1.encode('utf-8', 'ignore') + '\n')

        # Write content
        f1.write(str2.encode('utf-8','ignore') + '\n')
        f1.close()
