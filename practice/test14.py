#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import win32gui,win32api,win32con
br=webdriver.Firefox()
br.get("http://www.xnwmall.com")
br.maximize_window()
ActionChains(br).context_click(br.find_element_by_xpath("html/body/div[7]/div/div[3]/div[2]/ul/li[1]/a/img")).perform()
win32api.keybd_event(38,0,0,0)
win32api.keybd_event(38,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(38,0,0,0)
win32api.keybd_event(38,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(38,0,0,0)
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,win32con.KEYEVENTF_KEYUP,0)
