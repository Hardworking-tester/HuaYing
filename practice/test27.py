#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 8:53
import requests
import unittest
import time

# 接口信息
apixinxi = {
        '登录接口': {
                        '名称': '登录接口',
                        '地址': 'http://xxx/xxx/xx',
                        '请求类型': 'post'
                    },
        '参数': {
                    'username': 'Wbfxs001',
                    'password': '111111Qq',
                    'grant_type': 'password',
                },
        '期望值': {
                    'code': 200,
                    'name': 'Wbfxs001',
                    },
       }

# 常用参数不传，为空，整形，浮点，字符串，object,过短，超长，sql注入
objects1 = 'xxxx'
objects2 = 'ssss'
cycanshu = {
            '为空': [''],
            '整形': [10, 23, 44, 88, 99],
            '浮点': [1.11, 2.342, -1.03],
            '字符串': ['aaaa', 'bbbb', 'cccc','dddd'],
            'object': [objects1, objects2],
            '过短': ['1', '0'],
            '超长': ['11111111111111111111111111111111111111111111111'],
            'sql注入': [';and 1=1 ;and 1=2', ";and (select count(*) from sysobjects)>0 mssql", ";and 1=(select IS_SRVROLEMEMBER('sysadmin'));--"],
         }

# 得到cycanshu的key，将所有非正规参数放在一个list中
fzgcs = []
aaa = list(cycanshu.keys())
# print aaa
for i in aaa:
    # print(cycanshu[i])
    # 得到具体参数list
    bbb = cycanshu[i]
    for k in bbb:
        #便利每一个参数
        fzgcs.append(k)
# print(fzgcs)
# 拿到将要进行组合的参数
zhcs = dict(apixinxi['参数'])
# print "zhcs is :%s" %zhcs
# print(zhcs)
# 保存参数dict 为 list
print fzgcs
print zhcs
print zhcs.keys()
listall = []
for i in zhcs.keys():
    print "------------------%s---------------------" %i
    for k in fzgcs:
        print "@@@@@@@@@@@@@@@@@@@@@%s@@@@@@@@@@@@@@@@@@@@@" %k
        zhcs[i] = k
        print zhcs
        listall.append(zhcs)
        print listall
    print "****************************%s******************" %zhcs
# print(len(listall))
# print(listall)

# # 进行请求测试
# mp = requests.post(url=apixinxi['登录接口']['地址'], data=apixinxi['参数'])
# mpcode =  mp.status_code
# print(mpcode)
# assert mpcode == apixinxi['期望值']['code'], '实际返回参数：' + str(mpcode)

# 循环处理同一接口，不同参数反复请求