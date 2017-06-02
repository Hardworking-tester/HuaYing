# encoding:utf-8
import unittest, HTMLTestRunner
import time
import os
testlistdir = "G:\\HuaYing\\Action"

# print os.listdir(testlistdir)
# print os.listdir(testlistdir).__len__()
suite=[]
def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        testlistdir, pattern='test*.py',
        top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_suite)
    suite.append(testunit)
    return testunit
#
#
alltestcases = createsuite()
print alltestcases
print type(alltestcases)
print suite
print type(suite)
# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# filepath = "F:\\testresult\\" + now + "ResultReport.html"
# fp = file(filepath, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
# runner.run(alltestcases)
# fp.close()
