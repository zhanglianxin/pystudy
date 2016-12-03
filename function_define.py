#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义函数

def myabs(x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 如果没有 return 语句，
#  函数执行完毕后也会返回结果，只是结果为 None
#  return None 可以简写为 return

# 空函数
def nop():
    pass

# print myabs('8')

import math

# 返回多个值
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)

    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
# 假象 python 函数返回的仍然是单一值，返回值是一个 tuple 
r = move(100, 100, 60, math.pi / 6)
print r

# 在语法上，返回一个 tuple 可以省略括号，
#  而多个变量可以同时接收一个 tuple ，按位置赋值给对应的值。
#  所以，python 函数返回多值其实就是返回一个 tuple

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用 return 随之返回函数结果；
# 函数执行完毕也没有 return 语句时，自动 return None ；
# 函数可以同时返回多个值，但其实就是一个 tuple 。
