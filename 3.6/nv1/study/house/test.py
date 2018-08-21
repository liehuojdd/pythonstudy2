import time

time1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# Open and rewite, add file from beginning with 'w', add file from the end with 'a'
f1 = open('a1.txt', 'a')
f1.write(time1+'\n')
# encode as ASCII
for i in range(65,91):
    #str2=str1.encode('unicode')
    #f1.write(chr(i)+'\n')
    f1.write(chr(i)+'asasfasdfasdf'+str(33) + '\n')
#f1.write(myNote.encode('utf-8'))
f1.close()
