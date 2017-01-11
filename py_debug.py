#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
# main()
# 关闭断言 python -O py_debug.py 关闭后，可以把断言语句看成是 pass

# logging
import logging

# 指定记录信息的级别
logging.basicConfig(level = logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print 10 / n

# pdb python -m pdb py_debug.py

# pdb.set_trace() 在可能出错的地方设置一个断点
import pdb

s = '0'
n = int(s)
pdb.set_trace()
print 10 / n

# IDE 调试
