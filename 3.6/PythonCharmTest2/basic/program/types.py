'''
New in Python 3.0
https://blog.csdn.net/junchengberry/article/details/80841404

PEP 3113
Integer literals no longer support a trailing l or L.
String literals no longer support a leading u or U.
'''

a, b, c, d = 20, 5.5, True, 4+3j
#print(type(a), type(b), type(c), type(d))

a=10
b=51924361
c=15.20
d=1+2j
#print(type(b))

list1 = ['physics', 'chemistry', '1997', '2000']
print(len(list1))
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

#tuple
#tup1=(14)
tup1=(14,)
tup2=(14,"aaa","bbb",15)
print (tup2[1:3])
len(tup2)
tup1+tup2
tup1*2
print(tup2[-2])
print(tup2[1:])
print(tup2[:2])

m = list(range(100))
print(m[::10])