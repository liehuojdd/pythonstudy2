import random

def Add(list):
    total=20
    addlist=[]
    # m = random.randint(0, 10)  get an ramdom include 0 and 10
    writeinline=''

    for num in list:
        for i in range(num):
            addlist.append(str(i)+'+'+str(num-i)+'='+str(num))
            #print(str(i)+'+'+str(num-i))
            addlist.append(str(num - i) + '+' + str(i)+'='+str(num))
            #print(str(num - i) + '+' + str(i))

    for j in range(1,total):
        m=random.randint(0, len(addlist)-1)
        writeinline=writeinline+'\t'+addlist[m]
        if(j%4==0):
            print(writeinline)
            writeinline = ''

def Subtract(list,limit):
    total=20
    addlist=[]
    # m = random.randint(0, 10)  get an ramdom include 0 and 10
    writeinline=''

    for num in list:
        list2=range(limit+1)
        list=list2[-(limit-num)-1:]
        i=0
        for item in list:
            addlist.append(str(item)+'-'+str(i)+'='+str(num))
            i=i+1

    for j in range(1,total):
        m=random.randint(0, len(addlist)-1)
        writeinline=writeinline+'\t'+addlist[m]
        if(j%4==0):
            print(writeinline)
            writeinline = ''

if __name__=='__main__':
    Add([7,8])
    Subtract([6,7],10)