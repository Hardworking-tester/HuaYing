# encoding:utf-8
# author:wwg
from selenium import webdriver
from time import sleep
br=webdriver.Firefox()
br.get("http://background.xnwmall.com")
br.find_element_by_id("loginname").send_keys("scadmin")
br.find_element_by_id("password").send_keys("1")
sleep(5)
br.find_element_by_id("to-recover").click()
sleep(2)
br.find_element_by_link_text(u"活动").click()
sleep(2)
br.find_element_by_link_text(u"下单区域限制").click()
sleep(2)
br.find_element_by_xpath("/html/body/div/div/div/form/table[1]/tbody/tr/td[5]/input").click()
br.find_element_by_css_selector("button.btn-success").click()

