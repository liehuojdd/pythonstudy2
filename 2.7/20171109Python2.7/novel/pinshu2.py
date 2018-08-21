'''
Note: 12/12/2017
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
'''
from bs4 import BeautifulSoup
import mechanize
import time
import cookielib

class pinshu:
    url = 'https://www.vodtw.com/html/book/15/15248/6584416.html'
    urlEnd = '30885'#Seperate the page number by url
    fileName='test1.txt'
    pageTotal=1000
    sleepTime=0.5

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
        note = self.replaceStr(firstNote)
        # Save the first page
        self.saveAsFile(note)
        self.getContentForNextPage()

    def getContentForNextPage(self):
        i = 0
        for i in range(0, self.pageTotal):
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
            note = self.replaceStr(othersNote)
            # Save the note
            self.saveAsFile(note)

            # Print current page url
            urlNow = self.browser.geturl()
            urlNow = urlNow[urlNow.find(self.urlEnd) + len(self.urlEnd):]
            print 'Page total:'+ str(i) + ' of page ' + urlNow

    def replaceStr(self,string):
        # remove from beginning
        renote = ''
        strFind = '<br>'
        i=0
        str2 = str(string)
        str3 = str2[str2.find(strFind) + len(strFind):]
        # remove target <p>
        soup = BeautifulSoup(str3, "html5lib", from_encoding='utf-8')
        for element in soup.find_all('p'):
            # Keep the title with P
            if i == 0:
                renote = '<p>' + element.string + '</p>'
            renote = renote + element.string
            i=i+1
        return renote

    def saveAsFile(self,myNote):
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        f1=open(self.fileName,'a')
        f1.write(myNote.encode('utf-8'))
        f1.close()
