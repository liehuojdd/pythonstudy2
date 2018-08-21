import mechanize

#add certificate
browser=mechanize.Browser()
browser.add_client_certificate('url','key_file','cert_file')
browser.set_ca_data(cafile=None, capath=None, cadata=None, context=None)
browser.set_cookie("sid=abcdef; expires=Wednesday, 09-Nov-06 23:12:40 GMT")

#data to send with post
#time out, time out in seconds
browser.open('url or request',data='None',timeout=12000)
#Open url without visiting it
browser.open_novisit()

#go back, return response
response=browser.back(n=1)
response=browser.response()
browser.reload()
browser.retrieve('fullurl', filename=None, reporthook=None, data=None, timeout=12000, open='<built-in function open>')
browser.viewing_html()

#click
browser.click()
browser.click_link()

#return Cookie jar
mechanize.CookieJar

#Return iterable over forms
browser.forms()

#Return iterable over links
browser.links()

#Form
#class mechanize.HTMLForm(action, method='GET', enctype='application/x-www-form-urlencoded',
# name=None, attrs=None, request_class=<class mechanize._request.Request>, forms=None, labels=None, id_to_labels=None)[source]


