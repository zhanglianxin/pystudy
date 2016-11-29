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
