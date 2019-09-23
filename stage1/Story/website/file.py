import sys
'''
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
'''
class file:
    #encode = 'GBK'
    encode = 'UTF-8'
    def __init__(self,path):
        self.f1 = open(path, 'a',encoding=self.encode)

    def write(self,content):
        #self.f1.write(content.encode("GBK"))
        newcontent=str(content.encode(self.encode),encoding=self.encode)
        self.f1.write(newcontent)
        self.f1.write('\n')
    def close(self):
        self.f1.close()

