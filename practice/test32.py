# encoding:utf-8
# author:wwg
from selenium import webdriver
firefox_capabilities ={
    "browserName": "chrome",
    "version": "57.0.2987.133",
    # "browserName": "firefox",
    # "version": "52.0.2",
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
print type(firefox_capabilities)
browser=webdriver.Remote("http://192.168.178.135:5555/wd/hub",desired_capabilities=firefox_capabilities)
browser.get("http://www.baidu.com")
print browser.current_url
browser.get_screenshot_as_file("D:\\testdata\\baidu.png")
browser.close()