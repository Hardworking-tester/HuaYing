#coding=utf-8
#生成随机数
import random
list1=[]
q='176'

for qq in range(100):
    for i in range(8):
        m=str(random.randint(0,9))
        q=q+m

    if q.__len__()==11:
        if q not in list1:
            list1.append(q)
        q='176'
    # print q
    # if q in list1:
    #     continue
    # else:
    #     list1.append(q)


print list1
print list1.__len__()

