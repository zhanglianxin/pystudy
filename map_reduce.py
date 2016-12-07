#!/usr/bin/env python
# -*- coding: utf-8 -*-

# map() 函数
# 接收两个参数，一个是函数，一个是序列，map() 将传入的函数
#  依次作用到序列的每个元素，并把结果作为新的 list 返回。

def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# map() 作为高阶函数，事实上它把运算规则抽象了，因此，
#  不但可以计算简单的 f(x) = x * x ，还可以计算任意复杂的函数，
#  比如，把这个 list 所有数字转为字符串：
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# reduce() 函数
# 把一个函数作用在一个序列上，必须接收两个参数， reduce() 把结果
#  继续和序列的下一个元素做累积计算，其效果就是：
#  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 对一个序列求和，可以用 reduce 实现：
def add(x, y):
    return x + y
print reduce(add, [1, 3, 5, 7, 9])
# 把序列变成整数：
def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 3, 5, 7, 9])
# 把 str 转换为 int ：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7':7, '8':8, '9':9}[s]
print reduce(fn, map(char2num, '13579'))
# 整理成一个 str2int 函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7':7, '8':8, '9':9}[s]
    return reduce(fn, map(char2num, s))
# 还可以用 lambda 函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7':7, '8':8, '9':9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# TODO
# 利用 map() 函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#  输入：['adam', 'LISA', 'barT'] ，输出：['Adam', 'Lisa', 'Bart'] 。
def f(s):
    rst = ""
    for i in xrange(len(s)):
        if i == 0:
            rst = s[i].upper()
        else:
            rst += s[i].lower()
    return rst
print map(f, ['adam', 'LISA', 'barT'])
# Python 提供的 sum() 函数可以接收一个 list 并求和，请编写一个 prod() 函数，
#  可以接收一个 list 并利用 reduce() 求积。
def prod(x, y):
    return x * y
print reduce(prod, [1, 3, 5, 7, 9])
