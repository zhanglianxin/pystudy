#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 从索引 0 开始取，直到索引 3 为止，但不包括索引 3
print L[0 : 3] 
# 如果第一个的索引是 0 ，可以省略
print L[: 3]
# 倒数切片
print L[-2:]
print L[-2:-1]

# 创建一个 0 -- 99 的数列
L = range(100)
print L
print L[: 10]
print L[-10 :]
print L[10 : 20]
print L[: 10 : 2]
print L[:: 5]
print L[:] # 复制一个 list

# tuple 也是一种 list ，唯一区别是 tuple 不可变。
# 因此，也可用切片操作，结果仍是 tuple
print 'ABCDEFG'[: 3]
print 'ABCDEFG'[:: 2]

# 在很多编程语言中，针对字符串提供了很多各种截取函数，
#  其实目的就是对字符串切片。Python 没有针对字符串的截取函数，
#  只需要切片一个操作就可以完成，非常简单。
