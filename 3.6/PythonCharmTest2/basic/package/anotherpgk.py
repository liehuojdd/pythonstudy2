#from postjson.comm.JsonTest2 import JsonTest2
import postjson
from postjson.comm.JsonTest2 import JsonTest2 as pj

if __name__=='__main__':
    # newjson=JsonTest2("{}")
    newjson = postjson.JsonTest2.JsonTest2("{}")
    newjson.GetValue("")

    mypj=pj('{}')
    mypj.GetValue('')