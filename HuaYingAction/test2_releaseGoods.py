# encoding:utf-8
# author:
from HuaYingData import  get_number_by_data
from HuaYingData import ReadExcel
from HuaYingObject import LocateReleaseGoodsObject
from HuaYingOracle import Select
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
import unittest
import HTMLTestRunner
class ReleaseGoods():

    # def setUp(self):
    #     self.br=webdriver.Firefox()
    #     self.br.get("http://sso.xnwmall.com/mall/login.shtml")
    #     return self.br

    def getSendDataByCaseId(self,case_id):

        registerData_excel_path=r"G:\HuaYing\HuaYingData\releaseGoods_data.xls"
        caseid_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(registerData_excel_path,"releaseGoods_data",case_id)
        # print caseid_index
        preSend_data=[]
        loginName=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+2)
        loginPassword=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+3)
        productName=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+4)
        firstProductKeyWord=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+5)
        secondProductKeyWord=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+6)
        thirdProductKeyWord=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+7)
        productSummarize=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+8)
        productPicture=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+9)
        beginGuidance=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+10)
        endGuidance=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+11)
        proBeginWeight=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+12)
        proGW=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+13)
        attrNameVal=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+14)
        gAttrsC=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+15)
        marketPrice1=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+16)
        sellPrice=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+17)
        marketPrice2=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+18)
        reserve=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+19)
        productDetail=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+20)
        logisticsInformation=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"releaseGoods_data",caseid_index[0],caseid_index[1]+21)
        if type(loginName)==float:
            # print u"用户名为小数"
            preSend_data.append(str(int(loginName)))
        else:
            preSend_data.append(loginName)
        preSend_data.append(loginPassword)
        preSend_data.append(productName)
        preSend_data.append(firstProductKeyWord)
        preSend_data.append(secondProductKeyWord)
        preSend_data.append(thirdProductKeyWord)
        preSend_data.append(productSummarize)
        preSend_data.append(productPicture)
        preSend_data.append(beginGuidance)
        preSend_data.append(endGuidance)
        preSend_data.append(proBeginWeight)
        preSend_data.append(proGW)
        preSend_data.append(attrNameVal)
        preSend_data.append(gAttrsC)
        preSend_data.append(marketPrice1)
        preSend_data.append(sellPrice)
        preSend_data.append(marketPrice2)
        if type(reserve)==float:
            # print u"用户名为小数"
            preSend_data.append(str(int(reserve)))
        else:
            preSend_data.append(reserve)
        preSend_data.append(productDetail)
        preSend_data.append(logisticsInformation)
        return preSend_data

    #验证正常发布多规格商品功能
    def testSuccessReleaseGoods(self):
        """
        验证正常发布多规格商品功能
        """
        self.br=webdriver.Firefox()
        self.br.get("http://sso.xnwmall.com/mall/login.shtml")
        testCase_id="case_0008"
        print testCase_id
        send_data=self.getSendDataByCaseId(testCase_id)
        print send_data
        print send_data.__len__()
        loginName=send_data[0]
        loginPassword=send_data[1]
        productName=send_data[2]
        firstProductKeyWord=send_data[3]
        secondProductKeyWord=send_data[4]
        thirdProductKeyWord=send_data[5]
        productSummarize=send_data[6]
        productPicture=send_data[7]
        beginGuidance=send_data[8]
        endGuidance=send_data[9]
        proBeginWeight=send_data[10]
        proGW=send_data[11]
        attrNameVal=send_data[12]
        gAttrsC=send_data[13]
        marketPrice=send_data[14]
        sellPrice=send_data[15]
        marketPrice=send_data[16]
        reserve=send_data[17]
        productDetail=send_data[18]
        logisticsInformation=send_data[19]

        for i in send_data:
            print i

        LocateReleaseGoodsObject.LocateReleaseGoodsObject().getReleaseGoodsObject(self.br,send_data)

        # self.br.get_screenshot_as_file("G:\\pyresult\\image_SuccessRegister.png")
        # print("image_SuccessRegister.png")
        # if self.br.current_url=='http://user.xnwmall.com/register/registerByPhone.shtml' and self.br.find_element_by_css_selector("h2.f24").text==u'恭喜你注册成功':
        #     print u"从页面判断注册成功"
        #     if Select.Select().selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %phoneNumber)>0:
        #         print u"页面判断注册已成功，通过数据库已经查询到该用户信息，注册成功"
        #     else:
        #         print u"页面判断注册已成功，通过数据库查询无该用户，注册失败"
        # else:
        #     print u"从页面判断注册失败"
        #     if Select.Select().selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %phoneNumber)>0:
        #         print u"页面判断注册已失败，通过数据库已经查询到该用户信息，注册成功"
        #     else:
        #         print u"页面判断注册已失败，通过数据库查询无该用户，注册失败"





    def dealAlert(self,alertmessage):
        """处理错误信息"""
        #错误信息增加断言
        print (u"错误信息为：%s" %self.br.find_element_by_css_selector("span.text_error").text)
        print (u"预期错误信息为：%s" %alertmessage)
        if alertmessage==self.br.find_element_by_css_selector("span.text_error").text:
            return True
        else:
            return False

    def tearDown(self):
        self.br.close()


pp=ReleaseGoods()
pp.testSuccessReleaseGoods()