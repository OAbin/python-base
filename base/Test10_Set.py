# -*- coding: utf-8 -*-
# 集合测试-set,有序，key唯一
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
print s

#添加
s.add('Lucy')
print s

#删除
#s喊出最后一个
s.pop()
print s
#删除指定元素
s.remove('Lucy')
print s

#遍历
for ss in s:
    print ss