# encoding:utf-8
import urllib2,urllib
import json
import sys
import xlrd,time
class Send1318():

    def getExcelData(self):
        excle_path=r'G:\HuaYing\Data\sku.xls'
        table=xlrd.open_workbook(excle_path)
        sheet_name=table.sheets()[0]
        rows=sheet_name.nrows
        for i in range(1,2):
            try:
                price=int(sheet_name.cell_value(i,3))
                stock=int(sheet_name.cell_value(i,4))
                limit_min=int(sheet_name.cell_value(i,5))
                productId=int((sheet_name.cell_value(i,7)))
                goodsid=int(sheet_name.cell_value(i,8))
                supplyerId=sheet_name.cell_value(i,39)
                areaId=int(sheet_name.cell_value(i,0))
            except:
                pass
            # print price,stock,limit_min,productId,goodsid,supplyerId,areaId
            self.testSend1318(goodsid,supplyerId,productId,areaId,price,stock,limit_min,i)
        print "所有数据已对比完成"
    def testSend1318(self,goodsId,supplyerId,productId,areaId,price,stock,limit_min,i):
    # def testSend1318(self):
        """
        模拟发送1318指令
        """
        sys.stdout=open('G:\\pyresult\\data.txt','a')
        start = time.clock()
        post_url="http://item.huaqinwang.com/item/ajaxLoadSkuInfo.shtml"
        first_post_data={"goodsId":goodsId,
                         "specId":"",
                         "supplyerId":supplyerId,
                         "productId":productId,
                         "areaId":areaId}
        post_data=urllib.urlencode(first_post_data)
        req=urllib2.Request(post_url,post_data)
        rep=urllib2.urlopen(req)
        result=rep.read()
        # print result
        dataa=json.loads(result)
        # print type(dataa)
        try:
            return_stock=int(dataa['detailsmap']['product']['goodsInfoStock'])
            return_limit= int(dataa['detailsmap']['product']['areaCount'])
            return_price=int(dataa['detailsmap']['product']['goodsInfoPreferPrice'])
            print "服务器返回的商品库存为：%s        价格为：%s      最小起订量为：%s" %(return_stock,return_price,return_limit)
            print "永强提供的商品库存为：  %s        价格为：%s      最小起订量为：%s" %(stock,price,limit_min)
            if return_limit==limit_min and return_price==price and return_stock==stock:
                print "-----------------------------------exlce中第%s行数据核对已完成，数据核对结果：一致------------------------------------------" %(i+1)
            else:
                if return_limit!=limit_min:
                    print "------------------------------------exlce中第%s行数据核对已完成，数据核对结果：不一致,不一致的数据为:最小起订量--------------------------------------------------" %(i+1)
                if return_price!=price:
                    print "------------------------------------exlce中第%s行数据核对已完成，数据核对结果：不一致,不一致的数据为:价格--------------------------------------------------" %(i+1)
                if return_stock!=stock:
                    print "------------------------------------exlce中第%s行数据核对已完成，数据核对结果：不一致,不一致的数据为:库存--------------------------------------------------" %(i+1)

        except:
            print "------------------------------------exlce中第%s行数据核对出现异常--------------------------------------------------" %(i+1)
        end = time.clock()
        print "exlce中第%s行数据比对耗时 %f s" % ((i+1),(end - start))
        print "\n\n\n"


pp=Send1318()
pp.getExcelData()