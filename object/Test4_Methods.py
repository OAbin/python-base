# -*- coding: utf-8 -*-
#类的方法
class Person(object):

    name = 'xiaohong'

    #普通方法
    def getName(self):
        print "my name is xiaohong"

    #私有方法
    def _getName(self):
        print "my name is _xiaohong"

    #改变方法名称的类似私有方法
    def __getName(self):
        print "my name is __xiaohong"

    #类方法,类方法无法获得任何实例变量，只能获得类的引用。
    @classmethod
    def getClassMethod(cls):
        print "method is class method:" + cls.name

    #属性方法，将方法当做属性一样调用
    @property
    def getPropertyMethod(self):
        print "method is property method"


if __name__ == '__main__':
    person = Person()
    Person.getClassMethod()
    person.getPropertyMethod
    person.getName()