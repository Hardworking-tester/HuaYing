# encoding:utf-8
import urllib2,urllib
class Send1348():

    def testSend1348(self):
        """
        模拟发送1348指令
        """
        post_url="http://192.168.1.149:1101/chinaClearingNotify/mock13X8.do"
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"cfcaTxCode":"1348",
                         "status":"40",
                         "isTest":"1",
                         "paymentNo":"418e1458271442539YF8",
                         "orderNo":"1020160318397326504",
                         "amount":"100"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=Send1348()
pp.testSend1348()