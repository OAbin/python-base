# -*- coding: utf-8 -*-
# 集合测试-dict,有序，key唯一
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul':75
}

#添加
d['Lucy'] = 100

#删除
d.pop('Adam')

#遍历
print d.get('Adam')
print d['Lisa']

for k in d:
    print k + ':' , d.get(k)

