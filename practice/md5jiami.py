# encoding:utf-8
# author:wwg
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import hashlib
m=hashlib.md5()
m.update('6fbc95bc7919295b8b0074c3380e5e61')
psw = m.hexdigest()
print psw