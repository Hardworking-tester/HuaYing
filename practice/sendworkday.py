# encoding:utf-8
import urllib2,urllib,json
class Send1348():

    def testSend1348(self):
        """
        模拟发送1348指令
        """
        post_url="http://192.168.1.149:1131/workDay/add.do"
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"date":"20160902",
                         "workFlag":"w"}
        jdata = json.dumps(first_post_data)
        # post_data=urllib.urlencode(jdata)
        req=urllib2.Request(post_url,jdata)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=Send1348()
pp.testSend1348()