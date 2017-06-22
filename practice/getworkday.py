# encoding:utf-8
import urllib2,urllib
import requests,json
import urllib2, httplib, urllib, sys, cookielib, Cookie,cx_Oracle,uuid
class GetWorkDay():

    def testGetWorkDay(self):

        # con = cx_Oracle.connect('hqwsys', 'hqwbest_o0O', '192.168.10.3/huaqinbest')#正式环境
        con = cx_Oracle.connect('hqwsys', 'iw37l7vL', '192.168.1.149/huaqinw')#149测试环境
        con = cx_Oracle.connect('hqwsys', 'huaqinw', '192.168.1.131/huaqindevdb')  # 131测试环境
        cr = con.cursor()
        sql = "select mq.* from SYS_WORK_DAY mq order BY mq.CURRENT_DATE desc"
        cr.execute(sql)
        rs = cr.fetchone()
        # print type(rs)
        print u"数据库内当前最大日期为%s" %rs[1]
        oracle_time = int(rs[1])
        # print type(oracle_time)
        print "---------------------------------------------------------------------------------------"
        url = "http://192.168.10.5:1181/bankchannel/findWordDate.do"
        r = requests.post(url)
        # print type(r.text)
        dataa=json.loads(r.text)
        # print type(dataa)
        # print dataa
        value1=dataa['resultMsg']['statusText']
        # print value1
        i=0
        for dat in value1:
            deal_time=dat['date']
            work_flag=dat['workFlag']
            if int(deal_time)>oracle_time:
                print u"准备插入数据了"
                idd = str(uuid.uuid4()).replace('-', '')
                date1 = deal_time
                flag = work_flag
                sql2 = "INSERT INTO HQWSYS.SYS_WORK_DAY (ID, CURRENT_DATE, WORK_DAY_FLAG) VALUES " + "(" + "'" + idd + "'" + "," + "'" + date1 + "'" + "," + "'" + flag + "'" + ")"
                cr.execute(sql2)
                con.commit()
                i=i+1
                print u"插入的数据为%s" %date1
        print u"本次一共插入的数据为%s条" %i


pp=GetWorkDay()
pp.testGetWorkDay()