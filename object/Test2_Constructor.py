# -*- coding: utf-8 -*-
#类的构造函数
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


    #析构函数--销毁对象使用，垃圾回收
    def __del__(self):
        print "person is destory!"