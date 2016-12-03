#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 调用函数

# 数据类型转换
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool(2)
print bool(0)
print bool('')

# 函数名其实就是指向一个函数对象的引用，
#  完全可以把函数名赋给一个变量，
#  相当于给这个函数起了一个“别名”
a = abs
print a(-1)
