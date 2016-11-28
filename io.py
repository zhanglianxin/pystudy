#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入输出
name = raw_input('please enter your name:')
print 'hello', name
# 不支持接收输入 Unicode 字符集
name = raw_input(u'please enter your name:') # 输入中文
print 'hello', name
