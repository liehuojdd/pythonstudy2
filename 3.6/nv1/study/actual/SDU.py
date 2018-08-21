#Please follow the index of 5
#http://python.jobbole.com/81357/
'''
Because no user name and password, just study how to
post form and save cookie
'''
__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib.request
import http.cookiejar
import re

#山东大学绩点运算
class SDU:

    def __init__(self):
        self.loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
        #Save the cookies
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'xxxxxx'
         })
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request  = urllib.request.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        #打印登录内容
        print(result.read().decode('gbk'))

sdu = SDU()
sdu.getPage()