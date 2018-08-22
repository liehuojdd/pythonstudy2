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
    def __init__(self,path):
        self.f1 = open(path, 'a',encoding='GBK')

    def write(self,content):
        #self.f1.write(content.encode("GBK"))
        newcontent=str(content.encode("GBK"),encoding='GBK')
        self.f1.write(newcontent)
        self.f1.write('\n')
    def close(self):
        self.f1.close()

