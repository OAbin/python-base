# -*- coding: utf-8 -*-
#类的属性
class Person(object):

    #相当于静态属性，全局唯一
    id = "1321434"

    def __init__(self, name, age, score):
        self.name = name #普通属性
        self._age = age #私有属性
        self.__socre = score  # 会改变属性的名称，间接实现私有 ,可以通过_Person.__score来访问