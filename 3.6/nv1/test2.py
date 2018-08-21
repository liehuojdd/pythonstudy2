from com.package1.people import people
from com.package1.isdn import isdn
import urllib.parse
import urllib.request

request=urllib.request.Request("http://www.baidu.com")
response=urllib.request.urlopen(request)
print(response)
#Response
'''
valus={"username":"abc@test.com","password":"xxx"}
data=urllib.parse.urlencode(valus)
url="http://www.baidu.com"
response=urllib.request.Request(url,data)
request=urllib.request.urlopen(response)
'''
#Request
valus={"username":"abc@test.com","password":"xxx"}
data=urllib.parse.urlencode(valus)
url="http://www.baidu.com"
geturl=url+"?"+data
response=urllib.request.Request()
request=urllib.request.urlopen(response)