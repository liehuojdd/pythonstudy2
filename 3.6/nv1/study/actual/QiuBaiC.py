#Please follow the index of 2
#http://python.jobbole.com/81351/
import urllib.request
import re
import time
import _thread

class QiuBai:
    def __init__(self):
        self.pageIndex=1
        self.headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        self.stories=[]
        self.enable=False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib.request.URLError as e:
            print(e.reason)
            return None

    def getPageItems(self,pageIndex):
        try:
            content=self.getPage(self.pageIndex)
            if not content:
                return None
            pattern = re.compile('web-list-author-text.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>' +
                                 '.*?<i class="number">(.*?)</i>', re.S)
            items = re.findall(pattern, content)
            pageStories=[]
            for item in items:
                #pageStories.append(item[0].strip(),item[1].strip(),item[2].strip())
                pageStories.append(str(item[0])+str(item[1])+str(item[2]))
            return pageStories
        except urllib.request.URLError as e:
            print(e.reason)
            return None

    def loadPage(self):
        if self.enable==True:
            if len(self.stories)<2:
                pageStories=self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex+=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            #Python 2 row_input()
            keyword=input()
            self.loadPage()
            if keyword=="Q":
                self.enable=False
                return
            print(story)

    def start(self):
        self.enable=True
        self.loadPage()
        nowPage=0
        while self.enable:
            if len(self.stories)>0:
                pageStories=self.stories[0]
                nowPage+=1
                del self.stories[0]
                print('Please input Q to quite, and A for next:')
                self.getOneStory(pageStories,nowPage)

qiubai=QiuBai()
qiubai.start()