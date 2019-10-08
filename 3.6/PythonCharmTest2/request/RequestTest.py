import requests
#https://2.python-requests.org//en/master/
#r = requests.put('https://httpbin.org/put', data = {'key':'value'})
#r = requests.delete('https://httpbin.org/delete')
#r = requests.head('https://httpbin.org/get')
#r = requests.options('https://httpbin.org/get')

#payload = {'key1': 'value1', 'key2': 'value2'}
#payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
#r = requests.get('https://httpbin.org/get', params=payload)
#print(r.content) #body as bytes
#print(r.url)

#r = requests.get('https://api.github.com/events')
#r.encoding = 'ISO-8859-1'
#print(r.text)
#print(r.json()) #json data

r = requests.get('https://api.github.com/events', stream=True)
#print(r.raw)
#print(r.raw.read(10))

with open('myresponse.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)