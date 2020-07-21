# -*- coding: utf-8 -*-
#类的继承
class Person(object):
    name = 'xiaohong'
    def __init__(self, id, age):
        self.id = id
        self.age = age

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

#继承
class Student(Person):

    def __init__(self, id, age, score):
        super(Student, self).__init__(id, age)
        self.score = score


if __name__ == '__main__':
    student = Student("12344534", 12, 80)
    student.getName()
    print isinstance(student, Person)#判断是否是某一类型
    print issubclass(Student, Person)#判断是否是子类