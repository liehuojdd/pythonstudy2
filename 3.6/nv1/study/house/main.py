#!usr/bin/python
import study
import study.house
import study.house.singleprice
import study.house.house
from study.house.singleprice import singleprice
from study.house.house import house

if __name__ == '__main__':
    priceList=singleprice()
    #priceList.getByCode('http://www.tjfdc.com.cn/Pages/fcdt/HouseInfo.aspx?t=',
    #                'C50BF5AC2467&loupan=%E7%BB%8F%E7%BA%AC%E5%9F%8E%E5%B8%82%E7%BB%BF%E6%B4%B2%E6%AD%A6%E6%B8%85%E4%BA%8C%E6%9C%9F&projectname=%E5%AD%A6%E7%9F%A5%E5%8D%8E%E5%BA%AD31%E5%8F%B7%E6%A5%BC')
    house1=house()
    house1.main()


    b=1

