# encoding:utf-8
# author:wwg
import ConfigParser
import os

class ReadConfigFile():
    def get_value(self):
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取项目根目录的相对路径
        print root_dir

        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        url = config.get("firefox", "firefox_capabilities")
        print url
        # return url




trcf = ReadConfigFile()
trcf.get_value()