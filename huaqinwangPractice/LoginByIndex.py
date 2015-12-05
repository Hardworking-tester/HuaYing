# encoding:utf-8
# author:wwg
#首页登录
import time
from selenium import webdriver
br=webdriver.Firefox()
br.get("http://www.xnwmall.com")
br.find_element_by_id("login").click()
br.find_element_by_id("userName").send_keys('18638135380')
br.find_element_by_id("password").send_keys('wwg111')
br.find_element_by_id("subLoginBtn").click()
time.sleep(5)
if br.find_element_by_css_selector("span.login_infoQuit").text==u"退出":
    print "登录成功"