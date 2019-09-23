import requests
#https://2.python-requests.org//en/master/
r = requests.get('https://httpbin.org/get')
r.status_code
r.status_code == requests.codes.ok

r.headers
r.headers['Content-Type']
'application/json'

r.headers.get('content-type')
r.cookies['example_cookie_name']

url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')

r = requests.get(url, cookies=cookies)
r.text

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
url = 'https://httpbin.org/cookies'
r = requests.get(url, cookies=jar)
r.text

r = requests.get('http://github.com/')
#r = requests.get('http://github.com/', allow_redirects=False)

r.url
r.status_code
r.history

requests.get('https://github.com/', timeout=0.001)

