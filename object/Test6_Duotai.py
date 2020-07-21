# -*- coding: utf-8 -*-
#类的多太
class Person(object):
    name = 'xiaohong'
    def __init__(self, id, age):
        self.id = id
        self.age = age

    #普通方法
    def getName(self):
        print "my name is father"


#继承
class Student(Person):

    def __init__(self, id, age, score):
        super(Student, self).__init__(id, age)
        self.score = score

    def getName(self):
        print "my name is son"

#多太
def getName(person):
    if isinstance(person, Person):
        person.getName()


if __name__ == '__main__':
    person = Person("123", 12)
    student  = Student("234", 13, 80)
    getName(person)
    getName(student)
