#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 装饰器

# 由于函数也是一个对象，而且函数对象可以被赋值给变量，
#  所以，通过变量也能调用该函数。
# 函数对象有一个 __name__ 属性，可以拿到该函数的名字：
def now():
    print '2016-12-08'
f = now
f()
print now.__name__
print f.__name__

# 在代码运行期间动态增加功能的方式，称之为“装饰器”。
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 装饰器接收一个函数作为参数，并返回一个函数。
# 借助 Python 的 @ 语法，把装饰器置于函数的定义处：
@log
def now():
    print '2016-12-08'
# 调用 now() 函数，不仅会运行函数本身，还会在运行前打印一行日志：
now()
# 把 @log 放到 now() 函数的定义处，相当于执行了语句：
now = log(now)
# 由于 log() 是一个装饰器，返回一个函数，所以，原来的 now() 函数仍然存在，
#  只是现在同名的 now 变量指向了新的函数，于是调用 now() 将执行新函数，
#  即在 log() 函数中返回的 wrapper() 函数。

# wrapper() 函数的参数定义的是 (*args, **kw) ，因此， wrapper() 函数可以接受
#  任意参数的调用。在 wrapper() 函数内，首先打印日志，再紧接着调用原始函数。

# 如果装饰器本身需要传入参数，那就需要编写一个返回装饰器的高阶函数，写出来会更复杂。
#  比如，要自定义 log 的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' %(text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
# 这个三层嵌套的装饰器用法如下：
@log('execute')
def now():
    print '2016-12-08'
now()
# 和两层嵌套的装饰器相比，三层嵌套的效果是这样的
# now = log('execute')(now)
# 首先执行 log('execute') ，返回的是 decorator() 函数，再调用
#  返回的函数，参数是 now() 函数，返回值最终是 wrapper() 函数。

# 以上两种装饰器的定义都没有问题，但还差最后一步。
# 经过装饰器装饰之后的函数， __name__ 已经从原来的 'now' 变成了 'wrapper' ：
print now.__name__
# 因为返回的那个 wrapper() 函数名字就是 'wrapper' ，所以，需要把原始函数的
#  __name__ 等属性复制到 wrapper() 函数中，否则，有些依赖函数签名的代码执行就会出错。

import functools
def log(func):
    @functools.wrap(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 带参数的装饰器
def log(text):
    def decorator(func):
        @functools.wrap(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper
    return decorator

# 在面向对象的设计模式中，装饰器被称为装饰模式。
#  OOP 的装饰模式需要通过继承和组合来实现，
#  而 Python 除了能支持 OOP 的装饰器外，
#  直接从语法层次支持装饰器。Python 的装饰器
#  可以用函数实现，也可以用类实现。
# 装饰器可以增强函数的功能，定义起来虽然有点复杂，
#  但使用起来非常灵活和方便。

# 编写一个装饰器，能在函数调用的前后打印出 'begin call' 和 'end call' 的日志。

# 再思考能否写出一个 @log 的装饰器，使它既支持：
# @log
# def f():
#     pass
# 又支持：
# @log('execute')
# def f():
#     pass
