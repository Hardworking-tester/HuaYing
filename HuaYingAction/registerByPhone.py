# encoding:utf-8
# author:
from HuaYingData import  get_number_by_data
from HuaYingData import ReadExcel
from HuaYingObject import LocateRegisterObject
from HuaYingOracle import Select
from selenium import webdriver
from  selenium.webdriver.support.ui import WebDriverWait
import unittest
import HTMLTestRunner
class Register(unittest.TestCase):

    def setUp(self):
        self.br=webdriver.Firefox()
        self.br.get("http://www.xnwmall.com")
        return self.br

    def getRegisterDataByCaseId(self,case_id):

        registerData_excel_path=r"G:\HuaYing\HuaYingData\registerByPhoneNumber_data.xls"
        caseid_index=get_number_by_data.GetRowAndColNumber().getRowAndColNumber(registerData_excel_path,"register_data",case_id)
        # print caseid_index
        register_data=[]
        phoneNumber=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+2)
        firstPassword=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+3)
        secondPassword=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+4)
        pictureCheckCode=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+5)
        smsCheckCode=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+6)
        alertmessage=ReadExcel.ReadExcel().getDataByRowColIndex(registerData_excel_path,"register_data",caseid_index[0],caseid_index[1]+7)
        if type(phoneNumber)==float:
            # print u"用户名为小数"
            register_data.append(str(int(phoneNumber)))
        else:
            register_data.append(phoneNumber)
        register_data.append(firstPassword)
        register_data.append(secondPassword)
        register_data.append(pictureCheckCode)
        register_data.append(smsCheckCode)
        register_data.append(alertmessage)
        return register_data

    #验证正常注册功能
    def testSuccessRegister(self):
        """
        验证正常注册功能
        """
        testCase_id="case_0005"
        print testCase_id
        register_data=self.getRegisterDataByCaseId(testCase_id)
        phoneNumber=register_data[0]
        firstPassword=register_data[1]
        secondPassword=register_data[2]
        pictureCheckCode=register_data[3]
        smsCheckCode=register_data[4]
        alertmessage=register_data[5]

        LocateRegisterObject.LocateRegisterObject().getRegisterObject(self.br,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)

        self.br.get_screenshot_as_file("G:\\pyresult\\image_SuccessRegister.png")
        print("image_SuccessRegister.png")
        if self.br.current_url=='http://user.xnwmall.com/register/registerByPhone.shtml' and self.br.find_element_by_css_selector("h2.f24").text==u'恭喜你注册成功':
            print u"从页面判断注册成功"
            if Select.Select().selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %phoneNumber)>0:
                print u"页面判断注册已成功，通过数据库已经查询到该用户信息，注册成功"
            else:
                print u"页面判断注册已成功，通过数据库查询无该用户，注册失败"
        else:
            print u"从页面判断注册失败"
            if Select.Select().selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %phoneNumber)>0:
                print u"页面判断注册已失败，通过数据库已经查询到该用户信息，注册成功"
            else:
                print u"页面判断注册已失败，通过数据库查询无该用户，注册失败"


    #使用已经存在的手机号进行注册
    def testRegisterByExistPhoneNumber(self):
        """
        验证使用已经存在的手机号进行注册功能
        """
        testCase_id="case_0006"
        print testCase_id
        register_data=self.getRegisterDataByCaseId(testCase_id)
        phoneNumber=register_data[0]
        firstPassword=register_data[1]
        secondPassword=register_data[2]
        pictureCheckCode=register_data[3]
        smsCheckCode=register_data[4]
        alertmessage=register_data[5]

        LocateRegisterObject.LocateRegisterObject().getRegisterObject(self.br,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)

        self.br.get_screenshot_as_file("G:\\pyresult\\image_RegisterByExistPhoneNumber.png")
        print("image_RegisterByExistPhoneNumber.png")
        if self.br.current_url=='http://user.xnwmall.com/register/goRegister.shtml' and WebDriverWait(self.br,10).until(lambda br:self.br.find_element_by_xpath("//*[@id='regTelFrom']/div[1]/div[1]/ul[1]/li[2]/span[1]").text)==alertmessage:
            print u"注册失败，该手机号已经被注册，此用例执行成功"
        else:
            print u"使用已存在的手机号注册功能存在异常"

    #两次输入的密码不同进行注册
    def testRegisterByDifferentPassword(self):
        """
        验证使用两次输入的密码不同进行注册功能
        """
        testCase_id="case_0007"
        print testCase_id
        register_data=self.getRegisterDataByCaseId(testCase_id)
        phoneNumber=register_data[0]
        firstPassword=register_data[1]
        secondPassword=register_data[2]
        pictureCheckCode=register_data[3]
        smsCheckCode=register_data[4]
        alertmessage=register_data[5]

        LocateRegisterObject.LocateRegisterObject().getRegisterObject(self.br,phoneNumber,firstPassword,secondPassword,pictureCheckCode,smsCheckCode,alertmessage)

        self.br.get_screenshot_as_file("G:\\pyresult\\image_RegisterByDifferentPassword.png")
        print("image_RegisterByDifferentPassword.png")
        if self.br.current_url=='http://user.xnwmall.com/register/goRegister.shtml' and WebDriverWait(self.br,20).until(lambda br:self.br.find_element_by_xpath("//*[@id='regTelFrom']/div[3]/div[1]/ul[1]/li[2]/span[1]").text)==alertmessage:
            print u"注册失败，两次输入的密码不一致"
        else:
            print u"两次输入的密码不一致，注册功能存在异常"


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
