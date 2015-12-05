#encoding:utf-8
from selenium import webdriver
from time import sleep
import win32api, win32pdhutil, win32con
import win32com.client
from win32com.client import Dispatch
profile=webdriver.FirefoxProfile(r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\24iktfsp.test")
br=webdriver.Firefox(firefox_profile=profile)
br.get("http://sso.xnwmall.com/mall/login.shtml")
br.maximize_window()
sleep(5)
br.find_element_by_css_selector("input.text_input.text_input_h.input_xlarge").send_keys('13111111111')

br.find_element_by_id("password").send_keys("wwg111")
br.find_element_by_id("subLoginBtn").click()
sleep(5)
element1=br.find_element_by_link_text(u"商家入驻")
if element1.is_displayed():
    br.find_element_by_link_text(u"商家入驻").click()
else:

    br.refresh()
    br.find_element_by_link_text(u"商家入驻").click()
sleep(3)
br.switch_to_window(br.window_handles[-1])
br.find_element_by_id("settledTypeGYSSPAN").click()
br.find_element_by_css_selector("input[value='0'][ name='merCompanyProperty']").click()
br.find_element_by_id("merCompanyName_company").send_keys(u"自动化测试民营企业入驻")
br.find_element_by_css_selector("select.select_160.valid>")