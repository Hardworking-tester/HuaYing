# encoding:utf-8
# author:wwg
from selenium import webdriver
from time import sleep
import time
for i in range(1,100000):
    print i
    # br = webdriver.Firefox()
    br=webdriver.PhantomJS(executable_path='G:\\pyresult\\phantomjs-1.9.7-windows\\phantomjs.exe')
    br.get("http://www.hua-ying.com/")
    # print br.title
    sleep(2)
    if br.title ==u"无标题页":
        print time.ctime()
        br.quit()
        newbr=webdriver.Firefox()
        newbr.get("http://www.hua-ying.com/")
        newbr.maximize_window()
        sleep(5)
        # newbr.quit()
        break
    else:
        sleep(2)
        br.quit()
        sleep(2)