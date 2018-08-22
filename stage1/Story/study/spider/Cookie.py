#urllib2合并到了urllib下，
#urlopen使用时包的位置为urllib.request.urlopen，
#urlencode使用包位置为urllib.parse.urlencode
#cookielib变更为了http.cookiejar
import urllib.request
import http.cookiejar

filename="cookie.txt"
cookie=http.cookiejar.MozillaCookieJar(filename)
handler=urllib.request.HTTPCookieProcessor(cookie)
#平常的url open也是特殊的opener
opener=urllib.request.build_opener(handler)
response=opener.open("http://www.baidu.com")
#ignore_discard: save even cookies set to be discarded
#ignore_expires: save even cookies that have expiredThe file is overwritten if it already exists
cookie.save(ignore_discard=True,ignore_expires=True)

#Read cookies
cookie=http.cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req=urllib.request.Request("http://www.baidu.com")
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open(req)
print(response.read())

'''
The main sample, login and save cookies
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'stuid':'201200131012',
			'pwd':'23342321'
		})
#登录教务系统的URL
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
'''
