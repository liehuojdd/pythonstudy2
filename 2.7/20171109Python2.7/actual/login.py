import mechanize
import urllib
import urllib2
import cookielib
import os
import time
from PIL import Image

def login():
    url='http://www.baidu.com/index.php?tn=mswin_oem_dg'
    captchaUrl='http://www.baidu.com/img/bd_logo1.png'
    cookie=cookielib.CookieJar()
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    picture=opener.open(captchaUrl).read()
    local=open('logo.png','wb')
    local.write(picture)
    local.close()

    #Open photo viewer then close
    openedImg=Image.open('logo.png')
    openedImg.show()
    command='taskkill /F /IM dllhost.exe'
    time.sleep(2)
    os.system(command)

    a=1

if __name__=='__main__':
    login()
