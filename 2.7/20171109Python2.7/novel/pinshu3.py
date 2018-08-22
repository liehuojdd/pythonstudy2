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

class pinshu:

    url = b'5a15e50b2e5c7001ea7d08fe0c7f77d424f099920b932262d0b5e2dc5e930152fbb2ff47b7b5b36a957c564678feb63c4ac7e93a326ed37d44ef4f4d36ac9412'
    urlEnd = '30885'#Seperate the page number by url
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
        firstNote = self.soup.find(id='BookText')
        #firstNote = self.soup.find(attrs={'class':'p'})
        self.replaceStr(firstNote,'-1-')

        self.getContentWithException()

    def getContentWithException(self):
        while True:
            try:
                self.getContentForNextPage()
                if self.expCount >= self.expTotal:# Exception 3 times
                    break
            except Exception:
                time.sleep(3)
                self.expCount = self.expCount+1
                if self.expCount >= self.expTotal:# Exception 3 times
                    break
                else:
                    self.getContentWithException()
                print 'Exception at:' + str(self.expCount) + ' times '

    def getContentForNextPage(self):
            # Click next page
            # debug as links
            links=self.browser.links()
            time.sleep(self.sleepTime)
            nextpage = self.browser.find_link(text=u'\u4e0b\u4e00\u9875', tag=u'a')
            request = self.browser.click_link(nextpage)
            response = self.browser.open(request)
            # Get the content
            soup = BeautifulSoup(response, "html5lib")
            othersNote = soup.find(id='BookText')

            # Print current page url
            urlNow = self.browser.geturl()
            urlNow = urlNow[urlNow.find(self.urlEnd) + len(self.urlEnd):]
            self.replaceStr(othersNote,urlNow)
            self.pageTotal=self.pageTotal+1
            print 'Page total:'+ str(self.pageTotal) + ' of page ' + urlNow

    def replaceStr(self,string,urlNow):
        f1 = open(self.fileName, 'ab+')
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        # remove from beginning
        renote = ''
        strFind = '<br>'
        i=0
        str2 = str(string)
        str3 = str2[str2.find(strFind) + len(strFind):]
        # remove target <p>
        soup = BeautifulSoup(str3, "html5lib", from_encoding='utf-8')
        #str1='第 ' + urlNow + ' 章 '
        #str2='asdf'
        #f1.write(str1 + '\n')
        for element in soup.find_all('p'):
            # Remove the first title with p
            #if i == 0:
            #    # Write Title
            #    str1 = u'\u7b2c' + urlNow + u'\u7ae0' + element.string + u'\n'
            #    f1.write(str1.encode('utf-8','ignore')+'\n')
            #str4=element.string.encode('utf-8','ignore')

            # Fix bug if tag include element, goes to none
            if(element.string==None):
                renote = renote + str(element)
            else:
                renote = renote + element.string
            i=i+1
        str1 = u'\u7b2c' + urlNow + u'\u7ae0' + u'\n'
        f1.write(str1.encode('utf-8', 'ignore') + '\n')
        #Remove span
        span1=renote.replace('品书网 www.vodTw.com','')
        span1=span1.replace('本书来自 品书网 https://www.vodtw.com/html/book/30/30885/index.html','')
        span1 = span1.replace('品书网 www.vOdtw.com', '')
        span1 = span1.replace('品书网 www.voDtw.com', '')
        renote=span1
        # Write content
        f1.write(renote.encode('utf-8','ignore') + '\n')
        f1.close()
