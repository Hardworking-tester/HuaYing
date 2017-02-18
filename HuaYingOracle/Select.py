# encoding:utf-8
# author:wwg
import cx_Oracle
class Select():

    def selectData(self,sql):

        con=cx_Oracle.connect('mall','SUexr4bm','192.168.1.149/huaqinw')
        cr=con.cursor()
        cr.execute(sql)
        rs=cr.fetchall()
        countData=cr.rowcount
        # print countData
        return countData






# pp=Select()
# phoneNumber='15003991111'
# pp.selectData("select qt.* from mall_customer qt where qt.CUSTOMER_MOBILE=%s" %phoneNumber)
