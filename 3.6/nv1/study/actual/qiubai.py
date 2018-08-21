#Please follow the index of 1
#https://www.qiushibaike.com/hot/page/1/
import urllib.request
import re

page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
pattern=re.compile('web-list-author-text.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>'+
                   '.*?<i class="number">(.*?)</i>',re.S)
#re.S 任意匹配模式
content=response.read().decode('utf-8')
#print(content)
#If has image
#haveImg=re.search("img",item[3])
#if not haveImg:
#    print('')
items=re.findall(pattern,content)
for item in items:
 print(item[0],item[1],item[2])
