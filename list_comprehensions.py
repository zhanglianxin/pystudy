#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表生成式

L = []

# 生成 list [1 * 1, 2 * 2, ..., 10 * 10]
# 方法一 循环
for x in xrange(1, 11):
    L.append(x * x)
print L
# 方法二 列表生成式
print [x * x for x in xrange(1, 11)]
# for 循环后面加上判断，仅取偶数
print [x * x for x in xrange(1, 11) if x % 2 == 0]

# 使用两层循环生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下所有文件和目录名
import os
print [d for d in os.listdir('.')]

# for 循环同时迭代 key value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.iteritems():
    print k, ':', v
# 列表生成式使用两个变量来生成 list
print [k + ':' + v for k, v in d.iteritems()]
# 把 list 中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

# 运用列表生成式，可以快速生成 list ，
#  通过一个 list 推导出另一个 list ，而代码却十分简洁

L = ['Hello', 'World', 18, 'IBM', 'Apple']
print [s.lower() for s in L if isinstance(s, str)]

# 把 list 中所有的字符串变成小写，非字符串原样输出
print [s.lower() if isinstance(s, str) else s for s in L]
print [isinstance(s, str) and s.lower() or s for s in L]
