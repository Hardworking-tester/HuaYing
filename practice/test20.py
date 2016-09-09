#encoding:utf-8
import cx_Oracle
class OracleT1():


    def select1(self):
        con=cx_Oracle.connect('mall','huaqinw_8i9o','192.168.1.149/huaqinw')
        cr=con.cursor()
        sql="delete from mall_customer qt where qt.CUSTOMER_EMAIL='373391120@qq.com'"
        cr.execute(sql)
        con.commit()
        con.close()
        # rs=cr.fetchone()
        # print type(rs)
        # print rs
        # print rs[0]
pp=OracleT1()
pp.select1()