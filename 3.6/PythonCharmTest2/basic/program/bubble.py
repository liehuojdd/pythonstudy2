#/usr/bin/env python

list=[8,1,2,66,5,123]
def BubbleSort():
    for i in range(len(list)):
        print("i: "+str(i))
        '''
        i 0  j null
        i 1  j 0
        i 2  j 0 1
        i 3  j 0 1 2
        '''
        for j in range(i):
            print("j: "+str(j))
            if(list[j]>list[j+1]):
                list[j],list[j+1]=list[j+1],list[j]
    return list

if __name__=='__main__':
    list=BubbleSort()
    #print(list)