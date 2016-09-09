# encoding:utf-8
import urllib2,urllib
class Send1318():

    def testSend1318(self):
        """
        模拟发送1318指令
        """
        post_url="http://192.168.1.149:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"cfcaTxCode":"1318",
                         "status":"20",
                         "remark":"wwg",
                         "isTest":"1",
                         "paymentNo":"11181467680070386ZZM"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=Send1318()
pp.testSend1318()