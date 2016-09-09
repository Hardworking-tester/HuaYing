#encoding:utf-8
import cx_Oracle
class OracleT1():


    def select1(self,phone_number):
        con=cx_Oracle.connect('mall','huaqinw_8i9o','192.168.1.149/huaqinw')
        cr=con.cursor()
        # sql="select qt.* from mall_customer qt where qt.CUSTOMER_EMAIL='373391120@qq.com'"
        sql="select opp.* from MALL_COUPON_NO opp where opp.CUSTOMER_ID=(select oii.id from MALL_CUSTOMER oii where oii.CUSTOMER_MOBILE=%s)" %phone_number
        # sql="select oii.id from MALL_CUSTOMER oii where oii.CUSTOMER_MOBILE=%s" %phone_number
        cr.execute(sql)
        rs=cr.fetchall()
        if rs.__len__() ==5:
            print rs.__len__()
            print u"数据库查询注册成功并且注册已送券"
            # self.delete1()
        else:
            print u"数据库查询注册失败"
        # print rs
        con.close()
    def delete1(self):
        con=cx_Oracle.connect('mall','huaqinw_8i9o','192.168.1.149/huaqinw')
        cr=con.cursor()
        sql="delete from mall_customer qt where qt.CUSTOMER_EMAIL='373391120@qq.com'"
        cr.execute(sql)
        con.commit()
        self.select2()
        con.close()
        # rs=cr.fetchone()
        # print type(rs)
        # print rs
        # print rs[0]

    def select2(self):
        con=cx_Oracle.connect('mall','huaqinw_8i9o','192.168.1.149/huaqinw')
        cr=con.cursor()
        sql="select qt.* from mall_customer qt where qt.CUSTOMER_EMAIL='373391120@qq.com'"
        cr.execute(sql)
        rs=cr.fetchall()
        if rs.__len__()==0:
            print u"账号已删除，可以进行下一次注册操作"
        else:
            print u"账号删除失败"
        # print rs
        con.close()
pp=OracleT1()
pp.select1("15003999999")