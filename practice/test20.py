#encoding:utf-8
import cx_Oracle
class OracleT1():


    def select1(self):
        con=cx_Oracle.connect('mall','huaqinw_8i9o','192.168.1.131/huaqinw')
        cr=con.cursor()
        sql="select qq.id from mall_customer qq where qq.CUSTOMER_MOBILE='18638135380'"
        cr.execute(sql)
        rs=cr.fetchone()
        print type(rs)
        print rs
        print rs[0]
pp=OracleT1()
pp.select1()