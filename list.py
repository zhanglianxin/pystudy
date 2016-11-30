#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表 

# list 有序集合，可以随时添加和删除元素
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
# 获得元素个数
print 'length', len(classmates)
# 通过索引访问元素
for index in xrange(0, len(classmates)):
    print index, classmates[index]
# 从后往前负数做索引
for index in xrange(1, len(classmates) + 1):
    print -index, classmates[-index]
# 可变的有序表
# 追加元素到末尾
classmates.append('Adam')
print classmates
# 插入元素到指定索引
classmates.insert(1, 'Jack')
print classmates
# 删除末尾元素
classmates.pop()
print classmates
# 删除指定索引的元素
classmates.pop(1)
print classmates
# 替换指定索引的元素
classmates[1] = 'Sarah'
print classmates
# 数据类型可以不同
L = ['Apple', 123, True]
print L
# 元素可以嵌套另外的 list
s = ['python', 'java', ['asp', 'php'], 'schema']
print 'length', len(s)
p = ['asp', 'php']
s = ['python', 'java', p, 'schema']
print 'length', len(s)
# 空 list 长度是 0
L = []
print 'empty list length:', len(L)
print '---'

# list 特点
#   1. 查找和插入的时间随着元素的增加而增加
#   2. 占用空间小，浪费内存很少
