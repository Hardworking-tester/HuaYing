# encoding:utf-8
import urllib2,urllib,json
class Send1348():

    def testSend1348(self):
        """
        模拟发送1348指令
        """
        flag=False
        post_url="http://192.168.1.131:8431/user/login.json"
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"params":"{'email':'wwg82@163.com','pass':'wwg111'}"}
        # jdata = json.dumps(first_post_data)
        # print jdata
        # print type(jdata)
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result
        dict_result=json.loads(result)

        if dict_result['returnCode']==200:
            flag=True
        else:
            flag =flag
        # print flag
        # print dict_result
        return flag,dict_result