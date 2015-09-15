#encoding:utf-8
import urllib2,urllib
import cx_Oracle

# post_url="http://192.168.1.85:2010/mall-mobile/search/searchByKey.json"
# first_post_data={"params":{"key":"手机","sort":"0","sortType":"0","pageSize":"10","curPage":"1","pinpai":"","classes":"","startPrice":"0","endPrice":"10000"}}
# post_data=urllib.urlencode(first_post_data)
# req=urllib2.Request(post_url,post_data)
# rep=urllib2.urlopen(req)
# result=rep.read()
# print result
#




# post_url="http://192.168.0.85:2010/mall-mobile/search/searchByKey.json"
# first_post_data={"params":{"key":"手机","sort":"0","sortType":"0","pageSize":"10","curPage":"1","pinpai":"","classes":"","startPrice":"0","endPrice":"10000"}}
# post_data=urllib.urlencode(first_post_data)
# req=urllib2.Request(post_url,post_data)
# rep=urllib2.urlopen(req)
# result=rep.read()
# print result


for i in range(1,1001):
    post_url="http://192.168.1.85:2010/mall-mobile/login.json"
    first_post_data={"params":{"loginName":"15038163773","password":"123abc"}}
    post_data=urllib.urlencode(first_post_data)
    req=urllib2.Request(post_url,post_data)
    rep=urllib2.urlopen(req)
    result=rep.read()
    print result
    print "第%s次结果" %i

