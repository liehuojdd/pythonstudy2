#coding=utf-8
# SyntaxError: Non-ASCII character '\xe4'
from bs4 import BeautifulSoup
import mechanize
import time

note = ''
url = 'http://www.feizw.com/Html/10838/6662573.html'
urlEnd = '10838'

def main():
    note = ''
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    br = browser.open(url)

    soup = BeautifulSoup(br, "html5lib")
    firstNote = soup.find(id='content')
    note = note + replaceStr(firstNote)

    getContentForNextPage(browser)

    # Open and rewite, add file from beginning
    # f1=open('test1.txt','w')
    # Add file from the end.
    f1 = open('test1.txt', 'a')
    f1.write(note.encode('utf-8'))
    f1.close()

def getContentForNextPage(browser):
    i=0
    for i in range(0,5):
        # Click next page
        # debug as links
        # links=browser.links()
        nextpage = browser.find_link(text=u'\u4e0b\u4e00\u9875', tag=u'a')
        request = browser.click_link(nextpage)
        response = browser.open(request)
        # Get the content
        soup = BeautifulSoup(response, "html5lib")
        othersNote = soup.find(id='content')
        note = note + replaceStr(othersNote)
        urlNow = browser.geturl()
        urlNow = urlNow[urlNow.find(urlEnd) + len(urlEnd):]
        print 'Now getting page+ ' + urlNow
        time.sleep(0.5)

def replaceStr(string):
    #remove from beginning
    note='<p>'
    strFind = '-->'
    str2=str(string)
    str3=str2[str2.find(strFind) + len(strFind):]
    #remove <p>
    soup = BeautifulSoup(str3, "html5lib",from_encoding='utf-8')
    for element in soup.find_all('p'):
        note=note+element.string
    note = note + '</p>'
    return note

if __name__ == '__main__':
    main()


