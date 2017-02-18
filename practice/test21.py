# encoding:utf-8
# author:wwg
#使用邮箱注册账号，注册成功后删除
from selenium import webdriver
from oracle import delete
from time import sleep
# phone_list=['15003999988']
phone_list=['18900564864', '18968986792', '18904054096', '18959307759', '18928009256', '18907237780', '18955212880', '18963437831', '18975667014', '18914382550', '18926267758', '18997770849', '18901940612', '18950113749', '18947753515', '18991657315', '18992141376', '18982743089', '18928305293', '18952055233', '18974071122', '18996239098', '18941924443', '18950929664', '18987548596', '18952527602', '18905716138', '18950798576', '18907461992', '18985718765', '18943398465', '18983587803', '18964023096', '18984072726', '18929092112', '18970938999', '18993026249', '18990195710', '18925070785', '18963449087', '18937133477', '18903287335', '18951640616', '18997836718', '18965422562', '18902305409', '18997442918', '18942945923', '18983985251', '18967230473']
for i in range (phone_list.__len__()):
        #华禽网注册
        br=webdriver.Firefox()
        br.get("http://user.xnwmall.com/register/goRegister.shtml")
        # br.find_element_by_id("aaa2").click()
        sleep(1)
        br.find_element_by_id("phoneName").send_keys(phone_list[i])
        # br.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/form/div[2]/div/input").send_keys("wwgw")
        br.find_element_by_id("pwd").send_keys("wwg111")
        br.find_element_by_id("againCustomerPassword").send_keys("wwg111")
        br.find_element_by_id("eVerifyCodephone").send_keys("wwgs")
        br.find_element_by_css_selector("a.getTel_verBtn.c_333.getCode").click()
        sleep(1)
        br.find_element_by_css_selector("input.text_input.text_input_h.input_w_125.getTel_ver").send_keys("123456")
        br.find_element_by_id("regTelBtn").click()
        sleep(5)

        # if br.find_element_by_link_text(u"立即进入邮箱").is_displayed():
        #     print "通过页面元素查询注册成功"
        # else:
        #     print "通过页面元素查询注册失败"

        pp=delete.OracleT1().select1(phone_list[i])
        print u"这是第%s次执行手机号注册操作" %(i+1)
        br.quit()



print u"50次注册已经执行完毕"

