# encoding:utf-8
# author:wwg
import httplib
import urllib
import json
import urllib2
import re
import os
import sys
type = sys.getfilesystemencoding()

class BaiduImage(object):
    def __init__(self):
        super(BaiduImage, self).__init__()
        print u'图片获取中,CTRL+C 退出程序...'
        self.page = 30  # 当前页数
        if not os.path.exists(r'F:\testresult\image'):
            os.mkdir(r'F:\testresult\image')

    def request(self):
        try:
            while 1:

                conn = httplib.HTTPConnection('image.baidu.com')
                # request_url = '/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn=' + str(
                #     self.page)
                request_url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%80%A7%E6%84%9F%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%80%A7%E6%84%9F%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn=' + str(
                    self.page) + '&rn=30&gsm=1e00000000001e&1487928807461='
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                           'Content-type': 'test/html'}
                # body = urllib.urlencode({'tn':'resultjsonavatarnew','ie':'utf-8','word':'%E7%BE%8E%E5%A5%B3','cg':'girl','pn':self.page,'rn':'60'})
                conn.request('GET', request_url, headers=headers)
                r = conn.getresponse()
                # print r.status
                if r.status == 200:
                    data = r.read()
                    print "data is : %s" %data
                    data = unicode(data, errors='ignore')
                    decode = json.loads(data)
                    print "decode is : %s" %decode
                    self.download(decode['data'])

                self.page += 30
        except Exception, e:
            print e
        finally:
            conn.close()

    def download(self, data):
        print "data2 is : %s" %data
        for d in data:
            # url = d['thumbURL']   缩略图  尺寸200
            # url = d['hoverURL']           尺寸360
            print d
            if d:
                # print "-----------------"+str(d)+"----------------------------"
                url = d['hoverURL']
                data = urllib2.urlopen(url).read()
                # file_path=r"‪F:\testresult\tt.txt"
                # dd=open(r"d:\testresult\tt.txt",'wb')
                # data.decode("utf-8").encode(type)
                # print data
                # dd.write(data)
                # print "data3 is : %s" % data
                pattern = re.compile(r'.*/(.*?)\.jpg', re.S)
                item = re.findall(pattern, url)
                FileName = str('F:\\testresult\\image\\') + item[0] + str('.jpg')
                print "-----------------------------"+FileName+"---------------------------------"

                with open(FileName, 'wb') as f:
                    f.write(data)


if __name__ == '__main__':
    bi = BaiduImage()
    bi.request()
