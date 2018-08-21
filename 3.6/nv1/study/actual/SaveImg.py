#Please follow the index of 6
#http://python.jobbole.com/81359/
import urllib.request
import http.cookiejar
import os

def saveBrief(self,content,name):
    fileName = name + "/" + name + ".txt"
    f = open(fileName,"w+")
    print("正在偷偷保存她的个人信息为"+fileName)
    f.write(content.encode('utf-8'))

def mkdir(self,path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

#传入图片地址，文件名，保存单张图片
def saveImg(self,imageURL,fileName):
    u = urllib.urlopen(imageURL)
    data = u.read()
    f = open(fileName, 'wb')
    f.write(data)
    print("正在悄悄保存她的一张图片为"+fileName)
    f.close()