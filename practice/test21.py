# encoding:utf-8
# author:wwg
#使用邮箱注册账号，注册成功后删除
from selenium import webdriver
from oracle import delete
from time import sleep
# phone_list=['15003999988']
phone_list=['15486224471', '15403112070', '15402385161', '15447424590', '15402854156', '15471762002', '15470106171', '15488387683', '15408651671', '15488741767', '15454238660', '15454395853', '15494538310', '15412873086', '15425016787', '15492120914', '15425004560', '15442140508', '15480171268', '15467994968', '15416315661', '15433517813', '15408238559', '15406929237', '15482083349', '15457309032', '15422755755', '15409730940', '15450042093', '15462351742', '15456452378', '15470736232', '15455510326', '15417465318', '15474565565', '15422707765', '15454180845', '15473149833', '15456055484', '15406705737', '15413363385', '15431207097', '15473690680', '15433874158', '15487587892', '15434270470', '15406759556', '15415115334', '15423040462', '15491280610', '15484266987', '15487852600', '15448632573', '15450661078', '15457828946', '15470490057', '15499802172', '15401708070', '15447219555', '15428179816', '15495481658', '15464475401', '15445463737', '15428019428', '15444181545', '15449683741', '15411750252', '15436729482', '15411600786', '15468191957', '15449014486', '15459316399']
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

        # if br.find_element_by_link_text(u"立即进入邮箱").is_displayed():
        #     print "通过页面元素查询注册成功"
        # else:
        #     print "通过页面元素查询注册失败"
        br.close()
        pp=delete.OracleT1().select1(phone_list[i])
        print u"这是第%s次执行手机号注册操作" %(i+1)



print u"100次注册已经执行完毕"

