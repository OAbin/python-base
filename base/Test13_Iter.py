# -*- coding: utf-8 -*-
# 迭代测试
#list
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index+1, '-', name

#dict
#1、for
d = {
    'xiaohong': 90,
    'xiaobin' : 80,
    'xiaoming' : 70
}
for key in d:
    print key + ':',d.get(key)
#1、for value-区别是
# values() 方法实际上把一个 dict 转换成了包含 value 的list。
# 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存
for value1 in d.values():
    print value1
for value2 in d.itervalues():
    print value2

#for -key,value
#和 values() 有一个 itervalues() 类似， items() 也有一个对应的 iteritems()，
# iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() 不占用额外的内存。
for key1,value3 in d.items():
    print key1 + ':' , value3
for key2,value4 in d.iteritems():
    print key2 + ':' , value4