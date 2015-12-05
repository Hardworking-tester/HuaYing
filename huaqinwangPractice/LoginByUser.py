# encoding:utf-8
# author:wwg
#从登录页面登录
import time
from selenium import webdriver
br=webdriver.Firefox()
br.get("http://sso.xnwmall.com/mall/login.shtml")
br.find_element_by_id("userName").send_keys('18638135380')#用户名
br.find_element_by_id("password").send_keys('wwg111')#密码
br.find_element_by_id("subLoginBtn").click()#登录按钮
time.sleep(5)
if br.find_element_by_css_selector("span.login_infoQuit").text==u"退出":
    print "登录成功"
else:
    print "登录失败"