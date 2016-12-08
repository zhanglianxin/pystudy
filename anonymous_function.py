#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 匿名函数

# 在传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便。

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 匿名函数 lambda x: x * x 实际上就是：
# def f(x):
#     return x * x
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。

# 匿名函数有个限制，就是只能有一个表达式，不用写 return ，
#  返回值就是该表达式的结果

# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
#  此外，匿名函数也是一个函数对象，也可以把匿名函数赋
#  值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print f
f(5)

# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
