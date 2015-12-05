# encoding:utf-8
import urllib2,urllib
class CompulsoryTransfer():

    def testCompulsoryTransfer(self):
        """
        强制转账接口
        clientID:客户流水号，随便输入
        payAccNo=付款账号
        recvAccNo=收款账号
        recvAccNm=收款账户名称
        money=交易金额
        """

        post_url="http://192.168.1.149:1181/bankchannel/bankciticenforcepay.do"
        first_post_data={"clientID":"3812863",
                         "payAccNo":"3110710001371006607",
                         "recvAccNo":"3110710001371006786",
                         "recvAccNm":"押付宝集团",
                         "money":"0.01"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result


pp=CompulsoryTransfer()
pp.testCompulsoryTransfer()


