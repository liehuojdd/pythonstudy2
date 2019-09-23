import requests
import json
#https://2.python-requests.org//en/master/

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
ayload_dict = {'key1': ['value1', 'value2']}
#print(r.text)

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
data=json.dumps(payload)
print(data)
r = requests.post(url, data=json.dumps(payload))

url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
url = 'https://httpbin.org/post'
files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}


r = requests.post(url, files=files)
r.text
