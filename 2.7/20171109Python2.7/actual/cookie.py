import mechanize

def themain():
    #browser=mechanize.Browser()
    #browser.open('http://www.baidu.com')
    cj=mechanize.LWPCookieJar()
    opener=mechanize.build_opener(mechanize.HTTPCookieProcessor(cj))
    mechanize.install_opener(opener)
    r=mechanize.urlopen('http://www.baidu.com')
    cj.save('cookie.txt',ignore_discard=True,ignore_expires=True)


if __name__=='__main__':
    themain()