try:
    fh = open("testfile")
    fh.write("write")
#except IOError:
except BaseException:
    print ("Error")
else:
    print ("abc")
    fh.close()