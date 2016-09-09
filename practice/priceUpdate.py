# encoding:utf-8
# author:wwg
import xlrd
market_chart_data=""
date_data=""
huanan_data=""
huadong_data=""
huazhong_data=""
huabei_data=""
excel_path=r"F:\data\data20.xls"
print excel_path
data=xlrd.open_workbook(excel_path)
sheet_name=data.sheet_by_index(0)
cols=sheet_name.ncols
rows=sheet_name.nrows
# print u"该excel一共有%s列" %cols
print u"该excel一共有%s行" %rows
#取出日期的内容：
for i in range((rows-12),rows):
    date=str(sheet_name.cell_value(i,0)).split('.')[1]
    print i
    # print date
    date_data=date_data+date+'\,'
fina_date_data=date_data[:-2]
print "下面显示的是日期数据"
print fina_date_data
print "----------------------------------------------"
#取出华南地区数据：
for m in range((rows-12),rows):
    huanan=str(sheet_name.cell_value(m,1))
    print huanan
    huanan_data=huanan_data+huanan+'\,'
fina_huanan_data=huanan_data[:-2]
print "下面显示的是华南地区数据"
print fina_huanan_data
print "-------------------------------------------------------------"
#取出华东地区数据：
for w in range((rows-12),rows):
    huadong=str(sheet_name.cell_value(w,2))
    print huadong
    huadong_data=huadong_data+huadong+'\,'
fina_huadong_data=huadong_data[:-2]
print "下面显示的是华东地区数据"
print fina_huadong_data
print "----------------------------------------------------------------"
#取出华中地区数据：
for e in range((rows-12),rows):
    huazhong=str(sheet_name.cell_value(e,3))
    print huazhong
    huazhong_data=huazhong_data+huazhong+'\,'
fina_huazhong_data=huazhong_data[:-2]
print "下面显示的是华中地区数据"
print fina_huazhong_data
print "---------------------------------------------------------------"
#取出华北地区数据：
for r in range((rows-12),rows):

    huabei=str(sheet_name.cell_value(r,4))
    print huabei
    huabei_data=huabei_data+huabei+'\,'
fina_huabei_data=huabei_data[:-2]
print "下面显示的是华北地区数据"
print fina_huabei_data
print "-------------------------------------------------------------"



market_chart_data='{"华南":[{"categories":"'+fina_date_data+'"}\,{"data":"'+fina_huanan_data+'"\,"name":"毛鸭"}]\,"华东":[{"categories":"'\
                  +fina_date_data+'"}\,{"data":"'+fina_huadong_data+'"\,"name":"毛鸭"}]\,"华中":[{"categories":"'+fina_date_data+'"}\,{"data":"'\
                  +fina_huazhong_data+'"\,"name":"毛鸭"}]\,"华北":[{"categories":"'+fina_date_data+'"}\,{"data":"'\
                  +fina_huabei_data+'"\,"name":"毛鸭"}]}'
print 'market_chart_data=%s' %market_chart_data