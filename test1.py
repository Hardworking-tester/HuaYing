#encoding:utf-8
import urllib2,urllib
import cx_Oracle
# con=cx_Oracle.connect("pay", "pay","192.168.1.250/chinapay")
# cr=con.cursor()
# sql="select * from PAY_ACCOUNT"
# cr.execute(sql)
# rs=cr.fetchone()
# for m in rs:
#     print m
#
# print u"王伟高"
# post_url="http://192.168.1.85:2010/mall-mobile/search/searchByKey.json"
# first_post_data={"params":{"key":"手机","sort":"0","sortType":"0","pageSize":"10","curPage":"1","pinpai":"","classes":"","startPrice":"0","endPrice":"10000"}}
# post_data=urllib.urlencode(first_post_data)
# req=urllib2.Request(post_url,post_data)
# rep=urllib2.urlopen(req)
# result=rep.read()
# print result
#http://192.168.1.250:81/svn/HuaYing/sourcecode/mall-parent/mall-sso/target/classes/com/huaying/pay/sso/web/utils/Constant.class




post_url="http://192.168.1.131:2010/msg/sendPhoneMSG.json"
first_post_data={"params":{"messCodeType":"201","mobile":"17718880435"}}
post_data=urllib.urlencode(first_post_data)
req=urllib2.Request(post_url,post_data)
rep=urllib2.urlopen(req)
result=rep.read()
print result

#
# for i in range(1,1001):
#     post_url="http://192.168.1.85:2010/mall-mobile/login.json"
#     first_post_data={"params":{"loginName":"15038163773","password":"123abc"}}
#     post_data=urllib.urlencode(first_post_data)
#     req=urllib2.Request(post_url,post_data)
#     rep=urllib2.urlopen(req)
#     result=rep.read()
#     print result
#     print "第%s次结果" %i

