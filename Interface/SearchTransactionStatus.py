# encoding:utf-8
import urllib2,urllib
class SearchTransactionStatus():

    def testSearchTransactionStatus(self):
        """
        交易状态查询
        Transaction
        """
        post_url="http://192.168.1.149:1181/bankchannel/findpaystatus.do"
        #clientID：交易流水号
        first_post_data={"clientID":"324556"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=SearchTransactionStatus()
pp.testSearchTransactionStatus()