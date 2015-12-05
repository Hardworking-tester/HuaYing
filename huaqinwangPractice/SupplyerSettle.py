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
        br.find_element_by_id("userName").send_keys('18638135380')#用户名
        br.find_element_by_id("password").send_keys('wwg111')#密码
        br.find_element_by_id("subLoginBtn").click()#登录按钮
        time.sleep(5)
        if br.find_element_by_css_selector("span.login_infoQuit").text==u"退出":
            print "登录成功"
            return br
        else:
            print "登录失败"

    #测试民营企业入驻
    def minYingSettle(self):
        br=webdriver.Firefox()
        br.get("http://sso.xnwmall.com/mall/login.shtml")
        webBrowser=self.login(br)
        webBrowser.find_element_by_link_text(u"商家入驻").click()
        webBrowser.switch_to_window(webBrowser.window_handles[-1])
        webBrowser.find_element_by_id("settledTypeGYSSPAN").click()
        webBrowser.find_element_by_id("merCompanyName_company").send_keys(u"测试民营企业入驻")
        webBrowser.find_element_by_css_selector("select.select_160").find_element_by_css_selector("option[value='2']").click()
        webBrowser.find_element_by_css_selector("input[name='merCompanyType'][value='1']").click()
        webBrowser.find_element_by_css_selector("a.addBtn.fl").click()
        time.sleep(1)
        webBrowser.find_element_by_xpath("//*[@class='city_bottom']/div[1]/ul/li[1]/span").click()
        time.sleep(1)
        webBrowser.find_element_by_xpath("//*[@class='city_bottom']/div[1]/div[2]/dl/dd/span[1]").click()
        time.sleep(1)
        webBrowser.find_element_by_id("licenseRegisterNumber").send_keys("123342545")

        #
        autoit = Dispatch("AutoItX3.Control")
        str_filepath ="G:\\animal_white_baby_dogs_2_1920x1200_5693_2.jpg"
        webBrowser.find_element_by_id("licenseRegisterUPLOAD").click()
        webBrowser.find_element_by_css_selector("input[type='file']").click()
        autoit.WinWait(u"文件上传", "", 5)
        autoit.WinActivate(u"文件上传")
        autoit.ControlSetText(u"文件上传","","[CLASS:Edit; INSTANCE:1]",str_filepath)
        autoit.ControlClick(u"文件上传","",1) #附件上传动作
        time.sleep(2)
        webBrowser.find_element_by_css_selector("a.mot_btn_box._mask_upload").click()





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