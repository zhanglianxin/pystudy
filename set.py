#!/usr/bin/env python
# -*- coding: utf-8 -*-

# set 集合，只存储不重复的 key ，不存储 value

# 要创建一个 set ，需要提供一个 list 作为输入集合
s = set([1, 2, 3])
print s
# 重复元素在 set 中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print s
# 添加元素
s.add(4)
print s
s.add(4)
print s
# 删除元素
s.remove(4)
print s

# set 可以看成是无序、无重复元素的集合
#  可以做交集、并集操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
print '---'

# set 和 dict 的唯一区别仅在于没有存储对应的 value

# 不可变对象 str 是不可变对象 list 是可变对象
a = ['c', 'b', 'a']
a.sort()
print a

a = 'abc'
print a.replace('a', 'A')
print a

# 对于不可变对象来说，调用对象自身的任意方法，
#  也不会改变该对象自身的内容。
#  相反，这些方法会创建新的对象并返回，
#  这样，就保证了不可变对象本身永远是不可变的。
