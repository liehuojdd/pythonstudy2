import requests
from postjson.comm.JsonTest2 import JsonTest2

if __name__=='__main__':
    url = 'https://httpbin.org/post'
    payload = {'key1': 'value1'}
    r = requests.post(url, data=payload)
    #print(r.text)
    myJson=JsonTest2(r.text)
    str=myJson.GetValue("headers")
    str2 = myJson.GetValue("data")
    str3 = myJson.GetValue("files")