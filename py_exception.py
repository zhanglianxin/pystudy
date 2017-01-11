#!/usr/bin/env python
# -*- coding: utf-8 -*-

# try...exception...finally...
try:
    print 'try...'
    r = 10 / 0
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('a')
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivision:', e
finally:
    print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('8')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivision:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'
print '---'

# 所有的错误类型都继承自 BaseException 

# 调用堆栈

# 记录错误
# err.py
import logging

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
main()
print 'END'
# 同样是出错，但程序打印完错误后会继续执行，并正常退出。
# 通过配置， logging 还可以把错误记录到日志文件里，方便事后排查。

# 抛出错误
class FooError(StandardError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
def main():
    bar('0')
# main()

def foo(s):
    n = int(s)
    return 10 / n
def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise # 不带参数，把当前错误原样抛出。
        raise ValueError('input error!') # 把一种类型的错误转换成另一种类型
def main():
    bar('0')
main()
