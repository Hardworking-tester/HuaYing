#encoding:utf-8
from selenium import webdriver
from time import sleep
import time
import sys
sys.stdout=open(r"F:\picturedata\result.txt",'a')
br=webdriver.Firefox()

br.get('http://www.huaqinwang.com/search.shtml?searchKey=%E9%A1%BA&brand=&clazz=&pricebegin=0&priceend=0&sort=0&sorttype=0&areaId=240')
br.find_element_by_css_selector("li[data-code='240']").click()

sleep(3)
# print "王伟高"
# data1=br.find_element_by_css_selector("span.searchNum").text
# print "第一次进入页面后搜索结果数量为：%r"  %data1
# print time.ctime()
# br.get_screenshot_as_file(r"F:\picturedata\first.jpg")
# print "---------------------------------------------------------------------------------------"
i=4340
while True:

    try:
        sleep(30)
        br.refresh()
        print  "第%r次刷新页面后搜索结果数量为：%r" %(i,br.find_element_by_css_selector("span.searchNum").text)
        print time.ctime()
        picture="F:\\picturedata\\"+str(i)+".jpg"
        br.get_screenshot_as_file(picture)
        # br.get_screenshot_as_png()
        print "----------------------------------------------------------------------------------------------------"
        sys.stdout.flush()
        i=i+1
    except:
        print "搜到不到结果了"
