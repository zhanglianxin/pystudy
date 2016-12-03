#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数的参数

# 默认参数 降低了函数调用的难度
def power(x, n = 2):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s
print power(5, 3)

# 默认参数，必须指向不变对象！
def add_end(L = []):
    L.append('END')

    return L

print add_end()
print add_end()

def add_end1(L = None):
    if L is None:
        L = []
    L.append('END')

    return L

print add_end1()
print add_end1()
print '---'

# 为什么要设计 str None 这样的不变对象？
#  因为不变对象一旦创建，对象内部的数据就不能修改，
#  这样就减少了由于修改数据导致的错误。
#  由于对象不变，多任务环境下同时读取对象不需要加锁，
#  同时读一点问题都没有。
#  我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

# 可变参数
#  在函数内部，参数 接收到的是一个 tuple
def calc(*numbers):
    sum = 0
    for x in numbers:
        sum += x * x

    return sum

print calc(1, 2)
print calc()

# 如果已有一个 list 或 tuple ，调用一个可变参数
nums = [1, 2, 3]
print calc(*nums)
print '---'

# 关键字参数
#  可变参数允许传入 0 个或任意个参数，
#  这些可变参数在函数调用时自动组装为一个 tuple 。
#  关键字参数允许传入 0 个或任意个含参数名的参数，
#  这些关键字参数在函数内部自动组装为一个 dict 。

def person(name, age, **kw):
    print 'name:', name, 'age:', 'other:', kw
# 除了必须参数外，还接受关键字参数。
# 在调用该参数时，可以只传入必选参数。
person('Michael', 30)
# 也可以传入任意个数的关键字参数。
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 关键字参数有什么用？ 它可以扩展函数的功能。

# 和可变参数类似，也可以先组装出一个 dict ，
# 然后把该 dict 转换为关键字参数传进去
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)
print '---'

# 参数组合 
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
def func(a, b, c = 0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

# 函数调用时，解释器自动按照参数位置和参数名把对应的参数传进去
func(1, 2)
func(1, 2, c = 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x = 99)
# 通过一个 dict 和 tuple 也可以调用该函数
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
# 对于任意函数，都可以通过类似 `func(*args, **kw)` 的形式调用它，无论它的参数是如何定义的。
