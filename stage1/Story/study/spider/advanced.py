#http://python.jobbole.com/81349/
import urllib.request
import urllib.parse

#http://python.jobbole.com/81344/
#Build the header with user agent
url='http://www.server.com/login'
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
valuse={"usernaem":"cc","password":"xxx"}
headers={'User-Agent':user_agent}
#add heander with refer
headers = { 'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }
data=urllib.parse.urlencode(valuse)
request=urllib.request.Request(url,data,headers)
response=urllib.request.urlopen(request)

#Proxy
enable_proxy=True
#Python 2 urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
proxy_handler=urllib.request.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler=urllib.request.ProxyHandler({})
if enable_proxy:
    opener=urllib.request.build_opener(proxy_handler)
else:
    opener=urllib.request.build_opener(null_proxy_handler)

#Others
httpHandler = urllib.request.HTTPHandler(debuglevel=1)