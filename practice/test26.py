# encoding:utf-8
# author:wwg
import win32gui,win32api,win32con
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class Fruit:
    def __init__(self, color):
        self.color = color
        print "fruit's color: %s" % self.color

    def grow(self):
        print "grow..."


class Apple(Fruit):  # 继承了父类
    def __init__(self, color):  # 显示调用父类的__init__方法
        Fruit.__init__(self, color)
        print "apple's color: %s" % self.color


class Banana(Fruit):  # 继承了父类
    def __init__(self, color):  # 显示调用父类的__init__方法
        Fruit.__init__(self, color)
        print "banana's color:%s" % self.color

    def grow(self):  # 覆盖了父类的grow方法
        print "banana grow..."


if __name__ == "__main__":
    apple = Apple("red")
    apple.grow()
    banana = Banana("yellow")
    banana.grow()