#Please follow the index of 3
#http://python.jobbole.com/81353/
import urllib.request
import re
from study.actual.replaceWord import repliceWorld

class tieba:
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseUrl=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)
        self.floorTag=floorTag

    def getPage(self,pageNum):
        try:
            url=self.baseUrl+self.seeLZ+'?pn='+str(pageNum)
            headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            request=urllib.request.Request(url,headers=headers)
            response=urllib.request.urlopen(request)
            #print(response.read().decode('utf-8'))
            return response.read().decode('utf-8')
        except urllib.request.URLError as e:
            print(e.reason)
            return None

    def getTitle(self):
        page=self.getPage(1)
        pattern=re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
        #TypeError: cannot use a string pattern on a bytes-like object
        result=re.search(pattern,page)
        #result = re.search(pattern, str(page))
        if result:
            #print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return  None

    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num".*?<span class="red">(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            #print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return None

    def getContent(self,page):
        pattern = re.compile('class="d_post_content j_d_post_content ">(.*?)</div>', re.S)
        items=re.findall(pattern,page)
        contents=[]
        for item in items:
            content="\n"+repliceWorld().replace(item)+"\n"
            contents.append(content)
        return contents

    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+".txt","w+")
        else:
            self.file=open(self.defaultTitle+".txt","w+")

    def writeData(self,contents):
        for item in contents:
            #floorLine = "\n" + str(self.floor) + "------------"
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum()
        title=self.getTitle()
        #self.setFileTitle(title)
        print(type(title))
        self.setFileTitle(title)
        if pageNum==None:
            print('URL Wrong')
            return
        try:
            print('page total '+str(pageNum))
            for i in range(1,int(pageNum)+1):
                page=self.getPage(i)
                print('Writing page'+str(i))
                contents=self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print(e.reason)

baseUrl='http://tieba.baidu.com/p/5408054043'
#seeLZ=input()
#The floow info
floorTag=1
#Base URL, Only see LZ, The floow
bdtb=tieba(baseUrl,1,floorTag)
bdtb.start()