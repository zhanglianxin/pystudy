#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tuple 元组，有序列表，一旦初始化不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print classmates
# 可遍历获取元素，不能二次复制
# 获得元素个数
print 'length', len(classmates)
# 通过索引访问元素
for index in xrange(0, len(classmates)):
    print index, classmates[index]
# 从后往前负数做索引
for index in xrange(1, len(classmates) + 1):
    print -index, classmates[-index]
t = ()
print 'define empty tuple:', t
t = (1) # 此处被当作括号运算符
print 'define number:', t
t = (1, )
print 'define only one element:', t

# 不变 每个元素的指向永远不变，元素的本身可变
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t
