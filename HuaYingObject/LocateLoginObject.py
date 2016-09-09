#encoding:utf-8
import os
import sys,xlrd
from selenium.webdriver.common.by import By
from HuaYingData import ReadExcel,get_number_by_data
import OperateLoginElement
from Action import Browser
import time,OperateLoginElement
class LocateLoginObject():
    #该类主要是去定位登录功能中所用到的元素
    def getLocateObject(self,browser,username,password,errorMessage):
        """循环需要定位的元素，拿到一个元素之后去调用getLocatMethodAndData方法，取得元素的定位方式以及定位所需数据"""
        login_excel_path=r"G:\HuaYing\HuaYingData\login_data.xls"
        login_object_sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,"objname_locatemethod_locatedata")
        rows=login_object_sheet.nrows
        login_object_list=[]
        for i in range(rows):
            login_object_list.append(login_object_sheet.cell_value(i,0))
        # print login_object_list
        login_object_list.pop(0)
        # print login_object_list
        for login_object in login_object_list:
            self.getLocateMethodAndData(browser,login_object,username,password,errorMessage)



    def getLocateMethodAndData(self,browser,objname,username,password,errorMessage):
        """根据需要定位的元素的名称得到需要定位的元素的定位方式以及定位数据"""
        login_excel_path=r"G:\HuaYing\HuaYingData\login_data.xls"
        login_object_sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,"objname_locatemethod_locatedata")
        row_col_list=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(login_excel_path,"objname_locatemethod_locatedata",objname)
        old_how=login_object_sheet.cell_value(row_col_list[0],row_col_list[1]+1)
        what=login_object_sheet.cell_value(row_col_list[0],row_col_list[1]+2)
        #在这里增加一个字典是因为如果直接把By.ID写在excel里的话，取出来不能用
        locate_method_dict={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        new_how=locate_method_dict[old_how]
        self.locateElement(browser,new_how,what,objname,username,password,errorMessage)

    def locateElement(self,browser,how,what,obj_name,username,password,errorMessage):
        br=browser
        # print br
        located_element=br.find_element(by=how,value=what)
        OperateLoginElement.OperateElement().operateElement(br,obj_name,located_element,username,password,errorMessage)


