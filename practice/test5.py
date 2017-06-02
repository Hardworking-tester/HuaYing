# encoding:utf-8
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_usl="http://www.baidu.com"
    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.base_usl)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    file_path="F:\\result.html"
    fp =file(file_path,'wb')
    runner=HTMLTestRunner(stream=fp,title=u'百度测试报告',description=u'用例执行情况')
    runner.run(testunit)
    fp.close()