#encoding:utf-8
import urllib2,urllib
import json,ast,time
class InterfaceTest():


        def testT(self):
            phonelist=['17664247388', '17637328421', '17617166088', '17678766943', '17682968085', '17639040888', '17629122558', '17660649173', '17694079141', '17637815646', '17698948959', '17603063510', '17642395906', '17676017598', '17619571997', '17684154323', '17613874374', '17651578249', '17636326478', '17603574922', '17601949825', '17630358377', '17620079832', '17671661576', '17616378880', '17654116371', '17653071154', '17650568122', '17690420018', '17635284257', '17687838641', '17611058229', '17690315990', '17612169045', '17698782964', '17683928299', '17674332143', '17605174926', '17634029242', '17681128055', '17640584904', '17621656936', '17621046870', '17663124557', '17646024329', '17659473302', '17641086319', '17659245098', '17622491979', '17610197302', '17667903317', '17686510227', '17689797575', '17657076879', '17694071613', '17642872332', '17690189726', '17631071035', '17603455242', '17652872034', '17636902765', '17660417418', '17698663627', '17613415888', '17622881676', '17684204760', '17634702120', '17638974760', '17628833044', '17692846928', '17630838856', '17632789730', '17617571630', '17680003775', '17625626896', '17679935159', '17611734355', '17653796852', '17681340155', '17603267628', '17630358476', '17647869399', '17666992680', '17635422393', '17661270666', '17680933272', '17653591549', '17657893346', '17683119476', '17634760576', '17688242939', '17663746895', '17655148632', '17681402660', '17677923624', '17693824214', '17691524200', '17667026074', '17643257349', '17635867294']
            for i in range(phonelist.__len__()):
                print "第%s个手机号为：%s" %(i+1,phonelist[i])
                phonenumber=phonelist[i]
                print phonenumber
                self.test1(phonenumber)
        def test1(self,phonenumber):
            post_url="http://192.168.1.149:2010/msg/sendPhoneMSG.json"
            first_post_data={"params":{"messCodeType":"201","mobile":phonenumber}}
            post_data=urllib.urlencode(first_post_data)
            req=urllib2.Request(post_url,post_data)
            rep=urllib2.urlopen(req)
            result=rep.read()
            data=json.loads(result)
            rrr1=data['returnDatas']
            rrr2=eval(rrr1)
            messToken=rrr2['messToken']
            print messToken
            self.test2(messToken,phonenumber)
        def test2(self,messToken,phonenumber):


                post_url="http://192.168.1.149:2010/register/vaildMessageCode.json"
                first_post_data={"params":{"messCode":"123456","messCodeType":"201","messToken":messToken,"mobile":phonenumber,"sysType":"2"}}
                # print first_post_data
                post_data=urllib.urlencode(first_post_data)
                req=urllib2.Request(post_url,post_data)
                rep=urllib2.urlopen(req)
                result=rep.read()
                data=json.loads(result)
                rrr1=data['returnData']
                rrr2=eval(rrr1)
                valideToken=rrr2['valideToken']
                print valideToken
                self.test3(valideToken,phonenumber)
        def test3(self,valideToken,phonenumber):


            post_url="http://192.168.1.149:2010/register/savePassword.json"
            first_post_data={"params":{"confirmPass":"123456","mobile":phonenumber,"password":"123456","valideToken":valideToken}}
            post_data=urllib.urlencode(first_post_data)
            req=urllib2.Request(post_url,post_data)
            rep=urllib2.urlopen(req)
            result=rep.read()
            print result
            print  "手机号%s注册成功" %(phonenumber)
        time.sleep(2)

pp=InterfaceTest()
pp.testT()