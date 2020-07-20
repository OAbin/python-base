# -*- coding: utf-8 -*-
# 列表生成式测试
#生成一个list：1-11每个数的平方值
print [x * x for x in range(1, 11)]

#条件过滤
print [x * x for x in range(1, 11) if x % 2 == 0]

#多层表达式
print [n1*100+n2*10+n3 for n1 in range(1,10) for n2 in range (0,10) for n3 in range(0,10) if n1 == n3]