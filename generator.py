#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成器

# 在 Python 中，一边循环一边计算的机制，称为生成器

L = [x * x for x in xrange(10)]
print L
# 创建一个生成器 方法一
g = (x * x for x in xrange(10))
print g # 生成器保存的是算法
# 迭代生成器对象
for n in g:
    print n

# 斐波那契数列函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n += 1
fib(6)
# 创建一个生成器 方法二
# 斐波那契数列生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

for n in fib(6):
    print n

# 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个生成器    
# 生成器和函数的执行流程不一样。
# 函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。
# 而变成生成器的函数，在每次调用 next() 的时候执行，
#  遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。

# 理解生成器的工作原理
#  在 for 循环的过程中不断计算出下一个元素，并在适当的条件结束 for 循环。
#  对于函数改成的生成器来说， 遇到 return 语句或者执行到函数体最后一行语句，
#  就是结束生成器的指令， for 循环随之结束。
