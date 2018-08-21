#coding=utf-8

arr=[]
arr.append('')
arr.append('第1张 啥也不是')
arr.append('文字而已')
urlNow='ad'

f1=open('test2.txt','a')
str1 = u'\u7b2c' + urlNow + u'\u7ae0'
f1.write(str1.encode('utf-8')+urlNow+'\n')
f1.close()