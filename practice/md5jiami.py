# encoding:utf-8
# author:wwg
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import hashlib
m=hashlib.md5()
m.update('e99a18c428cb38d5f260853678922e03')
psw = m.hexdigest()
print psw