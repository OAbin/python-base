# -*- coding: utf-8 -*-
#测试获取对象信息的一些方法
class Person(object):
    name = 'xiaohong'
    def __init__(self, id, age):
        self.id = id
        self.age = age

    #普通方法
    def getName(self):
        print "my name is father"


if __name__ == '__main__':
    person = Person("123", 12)

    #获取类的类型 <class '__main__.Person'>
    print type(person)
    #获取类的定义属性 {'age': 12, 'id': '123'}
    print person.__dict__
    #获取类的所有属性，包括继承的 ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
    # '__hash__', '__init__', '__module__', '__new__','__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    # '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'getName', 'id', 'name']
    print dir(person)
    #获取属性
    print getattr(person, 'id')
    #设置属性
    setattr(person, 'id', '234')
    print getattr(person, 'id')

