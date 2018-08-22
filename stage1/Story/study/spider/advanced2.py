#http://python.jobbole.com/81344/
import urllib.request

#request = urllib.request.Request("http://blog.csdn.net/cqcra")
request = urllib.request.Request("http://www.wefaefsfaesf.com")
try:
    urllib.request.urlopen(request)
#except urllib.request.URLError:
#    print(urllib.request.URLError.reason)
except urllib.request.HTTPError as e:
    print("HTTPError: "+str(e.reason))
except urllib.request.URLError as e:
    print("URLError: "+str(e.reason))