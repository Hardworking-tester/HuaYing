# encoding:utf-8
# author:wwg
#用户注册
from selenium import webdriver
import time
br=webdriver.Firefox()
br.get("http://www.xnwmall.com")
br.find_element_by_link_text(u"免费注册").click()
time.sleep(2)
br.find_element_by_id("phoneName").send_keys("17677778875")#手机号
br.find_element_by_id("pwd").send_keys("wwg111")#密码
br.find_element_by_id("againCustomerPassword").send_keys("wwg111")#确认密码
br.find_element_by_id("eVerifyCodephone").send_keys("ffff")#图片验证码
br.find_element_by_css_selector("a.getTel_verBtn.c_333.getCode").click()#点击获取短信验证码
br.find_element_by_css_selector("input.text_input.text_input_h.input_w_125.getTel_ver").send_keys("123456")#输入短信验证码
br.find_element_by_id("regTelBtn").click()#点击提交注册
time.sleep(2)
if br.find_element_by_css_selector("h2.f24").text==u"恭喜你注册成功":
    print "手机号已注册成功"
    br.quit()