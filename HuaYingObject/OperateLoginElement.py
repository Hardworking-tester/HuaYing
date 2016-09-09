# encoding:utf-8
from selenium import webdriver
from HuaYingData import  ReadExcel,get_number_by_data
import time
class OperateElement():


    def operateElement(self,br,object_name,located_element,username,password,errorMessage):
        """该函数作用就是去操作已经定位到的元素，操作方式为sendkey或者click """
        login_excel_path=r"G:\HuaYing\HuaYingData\login_data.xls"
        login_operate_sheet=ReadExcel.ReadExcel().getTableBySheetName(login_excel_path,"operate_method")
        row_col_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(login_excel_path,"operate_method",object_name)
        operate_method=login_operate_sheet.cell_value(row_col_index[0],row_col_index[1]+1)
        # print operate_method
        # print object_name
        if operate_method=="click":
            located_element.click()
            time.sleep(2)
        elif operate_method=="sendkey" and object_name=="username":
            # print located_element
            # print username
            located_element.clear()
            located_element.send_keys(username)

            time.sleep(2)
        elif operate_method=="sendkey" and object_name=="password":
            located_element.send_keys(password)
            # print password
            time.sleep(2)

