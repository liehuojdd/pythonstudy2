#http://python.jobbole.com/81359/
import  re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'CQC! ohello')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
'''
if result1:
    # 使用Match获得分组信息
    print(result1.group())
else:
    print('1匹配失败！')

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print(result2.group())
else:
    print('2匹配失败！')

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print(result3.group())
else:
    print('3匹配失败！')

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print(result4.group())
else:
    print('4匹配失败！')
'''
#Word+Space+Word
pattern2 = re.compile(r'(\w+) (\w+)')
#m=re.match(pattern2,'? hello a world!')
m=re.match(pattern2,'hello a world!')
#if m:
#    print(m.string)
#else:
#    print('Failed')

'''
print("m.re:",m.re)
print("m.pos:",m.pos)
print("m.endpos:",m.endpos)
print("m.lastindex:",m.lastindex)
print("m.lastgroup:",m.lastgroup)
print("m.group():",m.group())
print("m.group(1,2):",m.group(1, 2))
print("m.groups():",m.groups())
print("m.groupdict():",m.groupdict())
print("m.start(2):",m.start(2))
print("m.end(2):",m.end(2))
print("m.span(2):",m.span(2))
print(r"m.expand(r'\g \g\g'):",m.expand(r'\2 \1\3'))
'''

#match是检测开头的位置，search是检测整个字符串
pattern=re.compile(r'world')
match=re.search(pattern,'hello world')
#match=re.match(pattern,'hello world')
#if match:
#    print(match.group())

pattern = re.compile(r'\d+')
str='one1two2three3four4'
#print(re.split(pattern,'one1two2three3four4'))
#print(re.findall(pattern,'one1two2three3four4'))
for m in re.finditer(pattern,str):
    print(m.group())
