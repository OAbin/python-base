# -*- coding: utf-8 -*-
# 集合测试-tuple
#创建后不可修改
#创建单个元素的tuple,加个 ,
t0 = (1 ,)

#创建多个元素tuple
t1 = (1, 2, 3)
print t1

#创建可修改的tuple
t2 = (1, 2, [3, 4, 5])
print t2
l = t2[2]
l.append(6)
print t2

