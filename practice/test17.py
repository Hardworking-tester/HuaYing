#encoding:utf-8
import xlrd
import sys
import time
from selenium import webdriver
excle_path=r'G:\HuaYing\Data\sku.xls'
table=xlrd.open_workbook(excle_path)
sheet_name=table.sheets()[0]
rows=sheet_name.nrows
# sys.stdout=open('G:\\pyresult\\data.txt','a')
# print u"此excel中共有%s行" %rows
base_url="http://item.huaqinwang.com/"
# dict1={21831}
for i in range(707,21831):
    start = time.clock()
    # print "第 %s行商品价格为：%s" %(i,int(sheet_name.cell_value(i,2)))
    price=int(sheet_name.cell_value(i,2))
    # print price
    # print "第 %s行商品库存为：%s" %(i,int(sheet_name.cell_value(i,3)))
    stock=int(sheet_name.cell_value(i,3))
    # print "第 %s行商品起订量为：%s" %(i,int(sheet_name.cell_value(i,4)))
    limit_min=int(sheet_name.cell_value(i,4))
    # print "第 %s行商品skuid为：%s" %(i,int(sheet_name.cell_value(i,7)))
    sku_id=int(sheet_name.cell_value(i,6))
    end_url=base_url+str(sku_id)+'.shtml'
    # print end_url
    # print "第 %s行商品所在市为：%s" %(i,sheet_name.cell_value(i,1))
    country=sheet_name.cell_value(i,0)
    province=sheet_name.cell_value(i,1)
    # print "-------------------------------以上数据为第%s条记录校验所需要所有字段-----------------------------------------------" %i
    # print u"第 %s行商品价格为：%s" %(i,sheet_name.cell_value(i,2))
    br=webdriver.Firefox()
    if province==u'全国省':
        print '全国省不核对'
    else:
        list1=[price,stock,limit_min,sku_id,end_url,country,province]
        print list1

        br.get(end_url)
        br.find_element_by_xpath("//*[@id='shadowAllCity']/div[2]/ul/li[4]").click()
        br.find_element_by_css_selector("span.findEditArea").click()
        br.find_element_by_xpath("//*[@id='detailMsg']/div[7]/div[1]/div[2]/div[2]/div[1]/ul/li[1]/span").click()
        elements1=br.find_elements_by_xpath("//*[@id='detailMsg']/div[7]/div[1]/div[2]/div[2]/div[2]/div[1]/span")
        for ii in elements1:
            if ii.text==province:
                ii.click()
        elements2=br.find_elements_by_xpath("//*[@id='detailMsg']/div[7]/div[1]/div[2]/div[2]/div[2]/div[2]/span")
        for m in elements2:
            if m.text==country:
                m.click()
        br.find_element_by_xpath("//*[@id='detailMsg']/div[7]/div[1]/div[2]/div[2]/div[2]/div[3]/span[1]").click()
        # print country
        # print province
        time.sleep(2)
        real_price=int((br.find_element_by_css_selector("span.det_pri_val").text)[:-3])
        real_stock=int(br.find_element_by_css_selector("em.stock_num").text)
        real_limit_min=int(br.find_element_by_id("min_buynum").text)
        list2=[real_price,real_stock,real_limit_min]
        print list2
        if real_price==price and real_limit_min==limit_min and real_stock==stock :
            print "-----------------------------------第%s次数据核对已完成，数据核对结果：一致------------------------------------------" %i
        else:
            print "------------------------------------第%s次数据核对已完成，数据核对结果：不一致--------------------------------------------------" %i
        # print "第%s次比对已完成"
        end = time.clock()
        print "read: %f s" % (end - start)
        br.close()
