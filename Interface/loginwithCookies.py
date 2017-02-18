# encoding:utf-8
import urllib2,urllib
import urllib2, httplib, urllib, sys, cookielib, Cookie
class Send1348():

    def testSend1348(self):
        """
        模拟发送1348指令
        """
        post_url="http://sso.huaqinwang.com/mall/login.shtml"
        cj = cookielib.CookieJar()
        print cj
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(post_url)
        # post_url="http://192.168.10.5:1101/chinaClearingNotify/mock13X8.do"
        first_post_data={"targetUrl":"",
                         "queryParams":"",
                         "loginCount":"1",
                         "isMemoried":"0@knet.cn",
                         "userName":"15673421345",
                         "password":"6fbc95bc7919295b8b0074c3380e5e61",
                         "code":"ooxx"}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        print result
        if '欢迎您登录' in result:
            print "----------------------------------------------"


        opener.addheaders = [('User-agent',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0')]
        urllib2.install_opener(opener)
        f=urllib.urlopen("http://sso.huaqinwang.com:80/mall/login.shtml")
        s=f.read()
        print s


pp=Send1348()
pp.testSend1348()