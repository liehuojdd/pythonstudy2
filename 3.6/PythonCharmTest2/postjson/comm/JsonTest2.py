import json

class JsonTest2:
    def __init__(self,json):
        self.json=json

    def GetValue(self,value):
        json_str = json.dumps(self.json)
        myjson=json.loads(json_str,encoding="utf-8") #first loads, get str type
        myjson = json.loads(myjson) # second loads, get dict type
        #print(type(myjson))
        for jvalue in myjson:
            if jvalue==value:
                return myjson[jvalue]
        pass