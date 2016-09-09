# encoding:utf-8
import urllib2,urllib
import requests,json
import urllib2, httplib, urllib, sys, cookielib, Cookie
class GetWorkDay():

    def testGetWorkDay(self):
        # """
        # 模拟发送1348指令
        # """
        # post_url="http://192.168.1.149:1181/bankchannel/findWordDate.do"
        # cj = cookielib.CookieJar()
        # print cj
        # opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        # urllib2.install_opener(opener)
        # resp = urllib2.urlopen(post_url)
        # # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        # first_post_data={"targetUrl":"",
        #                  "queryParams":"",
        #                  "loginCount":"1",
        #                  "isMemoried":"0@knet.cn",
        #                  "userName":"15673421345",
        #                  "password":"6fbc95bc7919295b8b0074c3380e5e61",
        #                  "code":"ooxx"}
        # # post_data=urllib.urlencode(first_post_data)
        # req=urllib2.Request(post_url)
        # rep=urllib2.urlopen(req)
        # result=rep.read()
        # print result
        url = "http://192.168.1.149:1181/bankchannel/findWordDate.do"
        r = requests.post(url)
        print type(r.text)
        dataa=json.loads(r.text)
        print type(dataa)
        value1=dataa['resultMsg']['statusText']
        print value1
        print type(value1)
        print value1[0]

pp=GetWorkDay()
pp.testGetWorkDay()