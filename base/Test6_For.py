# -*- coding: utf-8 -*-
# 循环测试-for
L = [2, 1, 2, 3]
sum = 0
for name in L:
    sum = sum + name;
print sum / 4

#while
x = 0
n = 5
while x < n:
    print x
    x = x + 1

#break、continue
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum +x
print sum

#多重循环
for x in [1,2,3,4,5,6,7,8,9 ]:
    for y in [ 0,1,2,3,4,5,6,7,8,9 ]:
        if x < y:
            print x * 10 + y