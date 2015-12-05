# -*- coding: utf-8 -*-
import urllib
import urllib2
url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"
req = urllib2.Request(url)
print req
res_data = urllib2.urlopen(req)
res = res_data.read()
print res
