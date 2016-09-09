#coding=utf-8
#生成随机数
import random
from HuaYingOracle import Select
list1=[]
q='189'

for qq in range(1000):
    for i in range(8):
        m=str(random.randint(0,9))
        q=q+m

    if q.__len__()==11:
        if q not in list1:
            if Select.Select().selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %q)==0:
                list1.append(q)
        q='189'
    # if list1.__len__()==100:
    #     break
    # print q
    # if q in list1:
    #     continue
    # else:
    #     list1.append(q)


print list1
print list1.__len__()

