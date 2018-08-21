'''
Note: 12/12/2017  Now can get page by page,
but can't get whole page. maybe the website server setting.
view by browser can get the whole page, don't know the reason.
'''
from bs4 import BeautifulSoup
import mechanize
import time
import cookielib

class feisu:
    note = ''
    #http://www.feizw.com/Html/10838/6662573.html
    url = 'http://www.feizw.com/Html/10838/6923530.html'
    urlEnd = '10838'
    fileName='test1.txt'
    pageTotal=2
    sleepTime=5

    # Find the content in - id='content'
    # Find the next page as - text=u'\u4e0b\u4e00\u9875', tag=u'a'
    # The content replace with function - replaceStr
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


    browser.set_handle_robots(False)
    br = browser.open(url)
    soup = BeautifulSoup(br, "html5lib")

    def __init__(self):
        a=1

    def main(self):
        firstNote = self.soup.find(id='content')
        self.note = self.note + self.replaceStr(firstNote)

        self.getContentForNextPage()

        self.saveAsFile()

    def getContentForNextPage(self):
        i = 0
        for i in range(0, self.pageTotal):
            # Click next page
            # debug as links
            # links=browser.links()
            time.sleep(self.sleepTime)
            nextpage = self.browser.find_link(text=u'\u4e0b\u4e00\u9875', tag=u'a')
            request = self.browser.click_link(nextpage)
            response = self.browser.open(request)
            # Get the content
            soup = BeautifulSoup(response, "html5lib")
            othersNote = soup.find(id='content')
            self.note = self.note + self.replaceStr(othersNote)
            # Print current page url
            urlNow = self.browser.geturl()
            urlNow = urlNow[urlNow.find(self.urlEnd) + len(self.urlEnd):]
            print 'Now getting page+ ' + urlNow

    def replaceStr(self,string):
        # remove from beginning
        renote = ''
        strFind = '-->'
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

    def saveAsFile(self):
        # Open and rewite, add file from beginning with 'w', add file from the end with 'a'
        f1=open('test1.txt','w')
        f1.write(self.note.encode('utf-8'))
        f1.close()
