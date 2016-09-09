# encoding:utf-8
# author:wwg
from selenium import webdriver
from time import sleep
import win32api, win32pdhutil, win32con
import win32com.client
from win32com.client import Dispatch

br=webdriver.Firefox()
br.get("http://www.xnwmall.com")
br.find_element_by_id("login").click()
br.find_element_by_id("userName").send_keys("15003991129")#用户名
br.find_element_by_id("password").send_keys("wwg111")#密码
br.find_element_by_id("subLoginBtn").click()
sleep(2)
br.find_element_by_link_text(u"商家入口").click()
br.switch_to_window(br.window_handles[-1])
sleep(2)
br.find_element_by_link_text(u"发布商品").click()
sleep(2)
br.find_element_by_css_selector("li[data-id='71e7fdb9714c4c30a320dedfc3b77a12']").click()
sleep(2)
br.find_element_by_css_selector("li[data-id='5bfa0e3cac16453a94de5d781562410a']").click()
sleep(2)
br.find_element_by_css_selector("li[data-id='41c8c551232a4a0a8553ea378a75da2e']").click()
sleep(2)
br.find_element_by_xpath("//*[@class='btn w_120 closeBox1']/strong[1]").click()
br.find_element_by_id("proName").send_keys(u"自动化发布商品3")#商品名称
br.find_element_by_css_selector("input.text_input.input_small.fl.keyword").send_keys("1")#关键词1
br.find_elements_by_css_selector("input.text_input.input_small.fl.marLeft_18.keyword")[0].send_keys("2")#关键词2
br.find_elements_by_css_selector("input.text_input.input_small.fl.marLeft_18.keyword")[1].send_keys("3")#关键词3
br.find_element_by_id("proDesc").send_keys(u"自动化发布商品概述2")#商品概述


str_filepath ="G:\\animal_white_baby_dogs_2_1920x1200_5693_2.jpg"
br.find_element_by_id("uploadimgList1SRC").click()
br.find_element_by_xpath("//*[@id='maskForm']/table/tbody/tr/td[2]/input").send_keys(str_filepath)#商品图片

sleep(2)
br.find_element_by_css_selector("a.mot_btn_box._mask_upload").click()
sleep(2)
br.find_element_by_id("CategoryBrandSelect").find_element_by_css_selector("option[value='64ede98bf82843b0b605631abfe60be4']").click()
br.find_element_by_id("proBeginPrice").send_keys("1")#最小指导价
br.find_element_by_id("proEndPrice").send_keys("12")#最大指导价
br.find_element_by_id("proJldw").find_element_by_css_selector("option[value='桶']").click()
br.find_element_by_id("proBeginWeight").send_keys("1")#起订量
br.find_element_by_id("proGW").send_keys("1")#毛重
br.find_element_by_css_selector("li[data-value='2']").click()
sleep(2)
#添加规格名称
br.find_element_by_id("attrAddBtn").click()
br.find_element_by_id("attrNameVal").send_keys("test2")#规格名
print br.find_element_by_css_selector("span.btn.f14")
# br.find_element_by_id("setAttrNameBtn").click()
sleep(4)
print "马上开始执行了"
br.find_element_by_css_selector("span.btn.f14").click()
print "wwg"
#添加规格值
sleep(3)
print br.find_elements_by_css_selector("span.hyFont.add_handle")
br.find_elements_by_css_selector("span.hyFont.add_handle")[-1].click()
sleep(2)
index=br.find_elements_by_css_selector("div.cho_attr.clearfix").__len__()
br.find_element_by_xpath("//*[@id='gAttrsC']/div[%s]/div/ul/li/span[2]/label/input" %index).send_keys("guigezhi3")#规格值
sleep(2)
br.find_elements_by_css_selector("a.confirm")[-1].click()
sleep(2)
br.find_elements_by_css_selector("input.i_chk")[-1].click()
sleep(2)
br.find_element_by_xpath("//*[@id='skuAttrBody']/tr[1]/td[3]/div[1]/input[1]").send_keys("33")#市场价
print "wwg1"
br.find_element_by_xpath("//*[@id='skuAttrBody']/tr[1]/td[2]/div[1]/input[1]").send_keys("2")#销售价

br.find_element_by_xpath("//*[@id='skuAttrBody']/tr[1]/td[3]/div[1]/input[1]").send_keys("33")#市场价

# print br.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/form/div[5]/div[2]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/input")
# br.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/form/div[5]/div[2]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/input").send_keys("2")
# print br.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/form/div[5]/div[2]/div[2]/div/div[2]/table/tbody/tr/td[2]/div/input").text
# print br.find_element_by_xpath("//*[@id='skuAttrBody']/tr[1]/td[2]/div[1]/input[1]").text
# sleep(3)
# print "wwg2"
# sleep(2)
br.find_element_by_xpath("//*[@id='skuAttrBody']/tr[1]/td[4]/div[1]/input[1]").send_keys("200")

js1="document.getElementsByClassName(\"ke-edit-iframe\")[0].contentWindow.document.body.innerHTML=\"%s\"" %("wwg1")
br.execute_script(js1)
br.find_elements_by_css_selector("span.ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-selectall")[0].click()
js2="document.getElementsByClassName(\"ke-edit-iframe\")[1].contentWindow.document.body.innerHTML=\"%s\"" %("wwg2")
br.execute_script(js2)
br.find_elements_by_css_selector("span.ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-selectall")[1].click()
# br.find_element_by_xpath("//*[@id='saveProBtn']/strong[1]").click()
# br.switch_to_alert().accept()