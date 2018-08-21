import mechanize
import webbrowser

#url = 'http://www.baidu.com'
#webbrowser.open(url)
#print webbrowser.get()
browser=mechanize.Browser()
browser.set_handle_robots(False)
br=browser.open('http://www.baidu.com')
browser.retrieve('http://www.baidu.com/img/bd_logo1.png','logo.png')
html=br.read()
local=open('D:/bak/workspace/20171109Python2.7/actual/logo.png','wb')
#local.write()
