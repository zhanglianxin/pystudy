#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sorted() 函数可以对 list 进行排序
print sorted([36, 5, 12, 9, 21])

# sorted() 函数也是一个高阶函数，可以接收一个比较函数来实现自定义排序。

# 定义一个倒序排序函数：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)

# 字符串排序 默认情况下，对字符串排序，是按照 ASCII 大小比较的
print sorted(['bob', 'about', 'Zoo', 'Credit'])

# 定义忽略大小写的比较算法：
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
