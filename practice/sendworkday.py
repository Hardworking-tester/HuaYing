# encoding:utf-8
import urllib2,urllib,json
class Send1348():

    def post(self):
        """
        发送post请求
        """
        post_url = "http://192.168.1.131:8431/user/isExistAccount.json"
        send_data = {"params":"{'email':'w1wg82@163.com','tel':'13099998876'}"}
        post_data = urllib.urlencode(send_data)
        req = urllib2.Request(post_url, post_data)
        rep = urllib2.urlopen(req)
        result = rep.read()
        dict_result = json.loads(result)

        if dict_result['returnCode'] == 200:
            print "success"
        else:
            print "failed"

pp=Send1348()
pp.post()