#!/usr/bin/python3
import json

if __name__=="__main__":
    # Python 字典类型转换为 JSON 对象
    data1 = {
    "args": {"key1": "value1"},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "no-cache",
        "Content-Length": "0",
        "Host": "httpbin.org",
        "Postman-Token": "505d5324-3a5f-493b-8595-a692d11a37b6",
        "User-Agent": "PostmanRuntime/7.3.0"
    },
    "json": "null",
    "origin": "123.151.200.131, 123.151.200.131",
    "url": "https://httpbin.org/post?key1=value1"
    }


    #new=data1["args"]  {'key1': 'value1'}
    for key in data1:
        print("=========")
        print(key)
        print(data1[key])
        print(type(data1[key])) 

    print(type(data1))
    json_str = json.dumps(data1) # formate data
    json_str = json.dumps(data1,indent=4)
    print("Python 原始数据：", repr(data1))
    print("JSON 对象：", json_str)
    print(type(json_str))

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])
    print(type(data2))