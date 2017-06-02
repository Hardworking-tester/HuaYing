# encoding:utf-8
# author:wwg
from selenium import webdriver
import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num

    def run(self):
        start=time.time()
        br=webdriver.Firefox()
        br.get("https://www.baidu.com")
        time.sleep(4)
        br.find_element_by_id("kw").send_keys("wwg")
        br.find_element_by_id("su").click()
        br.quit()
        end=time.time()
        print u'Thread Object(%d), Time:%s\n,耗时%s s' % (self.num, time.ctime(),(end-start))

def test():
    for i in range(1,10):
        t = MyThread(i)
        t.start()
        t.join()

if __name__=="__main__":
    test()