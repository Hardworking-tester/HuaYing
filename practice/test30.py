# encoding:utf-8
# author:wwg
import time
from selenium import webdriver

# i=0
for i in range(500):

        if i%2==0:
            try:
                print "偶数，开始正确性登录"
                br = webdriver.Firefox()
                br.get("http://sso.xunfangwang.com/goLogin.shtml")
                br.find_element_by_css_selector("input[name='email']").send_keys("373391120@qq.com")
                br.find_element_by_css_selector("input[name='pass']").send_keys("wwg111")
                br.find_element_by_id("J_submit").click()
                time.sleep(2)
                br.quit()
                i=i+1
            except:
                print "正确性登录出异常了"


        else:
            try:
                print "奇数，开始错误性登录"
                br = webdriver.Firefox()
                br.get("http://sso.xunfangwang.com/goLogin.shtml")
                br.find_element_by_css_selector("input[name='email']").send_keys("373391120@qq.com")
                br.find_element_by_css_selector("input[name='pass']").send_keys("wwg1111")
                br.find_element_by_id("J_submit").click()
                time.sleep(3)
                br.find_element_by_css_selector("a.tipbox_02_set").click()
                time.sleep(2)
                br.quit()
                i = i + 1
            except:
                print "错误性登录出异常了"