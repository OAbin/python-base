# -*- coding: utf-8 -*-
# 函数测试
#定义一个求集合每个元素的平方和
import math


def square_sum_list(L):
    sum = 0
    for l in L:
        square = l * l
        sum = sum + square
    return sum;


print square_sum_list([1, 2, 3])

#多返回值函数,返回一个tuple
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

#默认函数
def getName(name = 'xiaohong'):
    print 'hello' + name

getName()
getName('abin')

#可变函数
def varArgs(* args):
    print args

varArgs(1,2,3)
