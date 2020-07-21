# -*- coding: utf-8 -*-
#测试一些魔术方法,左右两边都带下划线的方法
#函数是通过魔术方法作用于对象的
class Person(object):

    def __new__(cls, *args, **kwargs):
        print 'object is new'
        return super(Person, cls).__new__(cls, *args, **kwargs)


    def __init__(self, name, age):
        print 'object is init'
        self.name = name
        self.age = age

    def __del__(self):
        print 'object is destory'

    #比较运算符
    def __cmp__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __eq__(self, other):
        if self.age == other.age:
            return True
        else:
            return False

    #数字运算符
    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    #逻辑运算符
    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    #tostring
    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    #只返回该类的属性 ，dir()函数作用于该magic method
    def __dir__(self):
        return self.__dict__.keys()

    #属性相关，setattr()函数作用于该magic method
    def __setattr__(self, key, value):
        pass

    def __getattr__(self, item):
        pass

    def __getattribute__(self, item):
        pass

    def __delattr__(self, item):
        pass


if __name__ == '__main__':
    person1 = Person("xiaohong", 12)
    person2 = Person("xiaobin", 13)

    print person1 == person2
    print person1 + person2

    print dir(person1)
    print person1

