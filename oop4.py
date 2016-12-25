#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 获取对象信息

# 使用 type() 函数判断对象类型
#  基本类型
print type(123) # <type 'int'>
print type('str') # <type 'str'>
print type(True) # <type 'bool'>
print type(None) # <type 'NoneType'>
#  函数类型、类类型
print type(abs) # <type 'builtin_function_or_method'>
class Animal(object):
    pass
a = Animal()
print type(a) # <class '__main__.Animal'>

import types
print type('abc') == types.StringType # True
print type(u'abc') == types.UnicodeType # True
print type([]) == types.ListType # True
print type(str) == types.TypeType # True
# 所有类型本身的类型就是 TypeType
print type(int) == type(str) == types.TypeType # True