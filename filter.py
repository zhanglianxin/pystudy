#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filter() 函数用于过滤序列
# 接收一个函数和一个序列，把传入的函数依次作用于每个元素，
#  然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。

# 在一个 list 中，删掉偶数，只保留奇数：
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15])

# 把一个序列的空字符串删掉：
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 可见用 filter() 这个高阶函数，关键在于正确实现一个“筛选”函数。

# 尝试用 filter() 删除 1 -- 100 的素数
import math
def not_sushu(n):
    flag = False
    if n <= 3:
        return n
    for x in xrange(3, math.trunc(math.sqrt(n))):
        if n % x == 0:
            flag = True
            continue
    if flag:
        return n
print filter(not_sushu, xrange(1, 101))
