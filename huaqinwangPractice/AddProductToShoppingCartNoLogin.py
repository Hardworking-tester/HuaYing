# encoding:utf-8
# author:wwg
from selenium import webdriver
br=webdriver.Firefox()
br.get("http://www.xnwmall.com")


br.find_element_by_xpath("//*[@class='sideFixedBar']/div[1]/ul[1]/li[1]/span[1]/i").click()