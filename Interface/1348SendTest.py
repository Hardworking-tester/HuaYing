# encoding:utf-8
import urllib2,urllib
class Send1348():

    def testSend1348(self):
        """
        模拟发送1348指令
        """
        # post_url="http://192.168.10.5:1101/messageCode.json"
        post_url = "http://192.168.1.149:1101/messageCode.json"
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"params":"{'sysType':'3','messCodeType':'301','userId':'111','mobile':'18638135380'}"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=Send1348()
pp.testSend1348()