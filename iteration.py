#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代

# 只要是可迭代对象，无论有无下标，都可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
# 迭代 dict
for key in d:
    print key
for value in d.itervalues():
    print value
for k, v in d.iteritems():
    print k, ':', v
# 迭代 字符串
for ch in 'ABC':
    print ch

# 如何判断一个对象是可迭代对象呢？
#  方法是通过 collections 模块的 Iterable 类型判断
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

# 实现下标循环
#  Python 内置的 enumerate() 函数可以把 list 变成索引-元素对，
#  这样就可以在 for 循环中同时迭代索引和元素本身。
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

# 任何可迭代对象都可以作用于 for 循环，包括自定义的数据类型，
#  只要符合迭代条件，就可以使用 for 循环
