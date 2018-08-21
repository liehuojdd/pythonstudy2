#http://python.jobbole.com/81344/
import urllib.parse
import urllib.request


request=urllib.request.Request("http://www.baidu.com")
#Python 2
#urllib2.urlopen("")
response=urllib.request.urlopen(request)
print(response)

#Form post
valus={"username":"abc@test.com","password":"xxx"}
#Python 2
#urllib.urlencode(values)
data=urllib.parse.urlencode(valus)
url="http://www.baidu.com"
response=urllib.request.Request(url,data)
request=urllib.request.urlopen(response)

#Form request
valus={"username":"abc@test.com","password":"xxx"}
data=urllib.parse.urlencode(valus)
url="http://www.baidu.com"
geturl=url+"?"+data
response=urllib.request.Request()
request=urllib.request.urlopen(response)