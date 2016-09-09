# encoding:utf-8
# author:wwg
#测试供应商入驻
from selenium import webdriver
import time
import win32api, win32pdhutil, win32con
import win32com.client
from win32com.client import Dispatch
class SupplySettle():

    def login(self,br):
        # br=webdriver.Firefox()
        # br.get("http://sso.xnwmall.com/mall/login.shtml")
        br.find_element_by_id("userName").send_keys('15699999999')#用户名
        br.find_element_by_id("password").send_keys('wwg111')#密码
        br.find_element_by_id("subLoginBtn").click()#登录按钮
        time.sleep(5)
        if br.find_element_by_css_selector("span.login_infoQuit").text==u"退出":
            print u"登录成功"
            return br
        else:
            print u"登录失败"

    #测试民营企业入驻
    def minYingSettle(self):
        br=webdriver.Firefox()
        br.get("http://sso.xnwmall.com/mall/login.shtml")
        webBrowser=self.login(br)
        webBrowser.find_element_by_link_text(u"商家入驻").click()#点击工具条商家入驻链接

        #关闭上级页面并切换句柄至当前页面
        webBrowser.switch_to_window(webBrowser.window_handles[-1])
        webBrowser.switch_to_window(webBrowser.window_handles[0])
        webBrowser.close()
        webBrowser.switch_to_window(webBrowser.window_handles[-1])


        webBrowser.find_element_by_id("settledTypeGYSSPAN").click()#选择入驻类型为：供应商
        # webBrowser.find_element_by_xpath("//*[@class='controls clearfix enterProperty']/label[1]/input").click()#选择入驻的企业性质：民营企业
        # webBrowser.find_element_by_id("merCompanyName_company").send_keys(u"测试民营企业入驻1")#企业名称输入框
        # webBrowser.find_element_by_css_selector("select.select_160").find_element_by_css_selector("option[value='2']").click()#商家类型选择
        # webBrowser.find_element_by_css_selector("input[name='merCompanyType'][value='1']").click()#企业类型选择


        #配送区域选择
        # webBrowser.find_element_by_css_selector("a.addBtn.fl").click()
        # time.sleep(1)
        # webBrowser.find_element_by_xpath("//*[@class='city_bottom']/div[1]/ul/li[1]/span").click()
        # time.sleep(1)
        # webBrowser.find_element_by_xpath("//*[@class='city_bottom']/div[1]/div[2]/dl/dd/span[1]").click()
        # time.sleep(1)


        # webBrowser.find_element_by_id("licenseRegisterNumber").send_keys("123342545")#营业执照号码输入框


        autoit = Dispatch("AutoItX3.Control")
        #上传营业执照
        str_filepath ="G:\\animal_white_baby_dogs_2_1920x1200_5693_2.jpg"
        webBrowser.find_element_by_id("licenseRegisterUPLOAD").click()
        webBrowser.find_element_by_css_selector("input[type='file']").click()

        # print autoit.WinExists(u"文件上传")
        autoit.WinWait(u"文件上传", "")

        print u"窗口已找到"
        autoit.WinActivate(u"文件上传")

        print u"窗口已激活"

        autoit.ControlFocus(u"文件上传","","[CLASS:Edit; INSTANCE:1]")
        print u"输入框已定位到"
        autoit.ControlSetText(u"文件上传","","[CLASS:Edit; INSTANCE:1]",str_filepath)

        print u"文件路径已传入"
        autoit.ControlClick(u"文件上传","",1) #附件上传动作
        time.sleep(2)
        webBrowser.find_element_by_css_selector("a.mot_btn_box._mask_upload").click()
        # webBrowser.find_element_by_xpath("//*[@id='maskForm']/a[1]").click()
        time.sleep(5)

        webBrowser.find_element_by_css_selector("input[name='organizationCode']").send_keys("34566")#组织机构代码输入框
        #上传组织结构代码证
        # str_filepath1 ="G:\\animal_white_baby_dogs_2_1920x1200_5693_2.jpg"
        # webBrowser.find_element_by_id("organizationFrontalUPLOAD").click()
        # webBrowser.find_element_by_css_selector("input[type='file']").click()
        # autoit.WinWait(u"文件上传", "", 5)
        # autoit.WinActivate(u"文件上传")
        # autoit.ControlSetText(u"文件上传","","[CLASS:Edit; INSTANCE:1]",str_filepath1)
        # autoit.ControlClick(u"文件上传","",1) #附件上传动作
        # time.sleep(2)
        # webBrowser.find_element_by_css_selector("a.mot_btn_box._mask_upload").click()
        #
        # time.sleep(5)
        # webBrowser.find_element_by_css_selector("input[name='taxRegisterNumber']").send_keys("789788k")#税务登记证号码输入框
        # #上传税务登记证
        # str_filepath2 ="G:\\animal_white_baby_dogs_2_1920x1200_5693_2.jpg"
        # webBrowser.find_element_by_id("taxRegisterUPLOAD").click()
        # webBrowser.find_element_by_css_selector("input[type='file']").click()
        # autoit.WinWait(u"文件上传", "", 5)
        # autoit.WinActivate(u"文件上传")
        # autoit.ControlSetText(u"文件上传","","[CLASS:Edit; INSTANCE:1]",str_filepath2)
        # autoit.ControlClick(u"文件上传","",1) #附件上传动作
        # time.sleep(2)
        # webBrowser.find_element_by_css_selector("a.mot_btn_box._mask_upload").click()
        #
        # webBrowser.find_element_by_css_selector("input[name='cardOwner']").send_keys(u"测试民营企业入驻银行账户名")#银行账户名输入框
        # webBrowser.find_element_by_id("cardNo").send_keys("6226901108962010")#银行账号输入框
        # webBrowser.find_element_by_css_selector("input[name='openBankName']").click()#开户行文本框
        # time.sleep(2)
        #
        # #开户行所在支行选择
        # webBrowser.find_element_by_css_selector("input[name='openBranchName']").click()
        # webBrowser.find_element_by_xpath("//*[@data-code='102307208555']/span").click()
        # webBrowser.find_element_by_id("branch_sure_btn").click()
        #
        #
        # webBrowser.find_element_by_id("openSubLocation").send_keys(u"郑汴路支行")
        # webBrowser.find_element_by_css_selector("input[name='contactName']").send_keys(u"测试民营企业入驻1")
        # webBrowser.find_element_by_css_selector("input[name='contactPhone']").send_keys("18638135366")
        # webBrowser.find_element_by_css_selector("input[name='contactEmail']").send_keys("2345565@qq.com")
        # webBrowser.find_element_by_id("contactAddress").send_keys(u"盛润国际")
        # webBrowser.find_element_by_id("enterforma").click()



    #测试国有企业入驻
    def guoYouSettle(self):
        pass

    #测试外资企业入驻
    def waiZiSettle(self):
        pass

    #测试个体工商户入驻
    def geTiSettle(self):
        pass

    #测试个人入驻
    def geRenSettle(self):
        pass


pp=SupplySettle()
pp.minYingSettle()