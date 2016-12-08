#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 返回函数 函数作为返回值

# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。

# 定义求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax
# 如果不需要立即求和，而是在后面的代码中，根据需要再计算。
# 可以不返回求和的结果，而是返回求和的函数。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum
# 当调用 lazy_sum() 时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 3, 5, 7, 9)
print f
# 调用函数 f() 时，才真正计算求和的结果：
print f()

# 在这个例子中，在函数 lazy_sum() 中又定义了函数 sum() ，并且，
#  内部函数 sum() 可以引用外部函数 lazy_sum() 的参数和局部变量，
#  当 lazy_sum() 返回函数 sum() 时，相关参数和变量都保存在返回的函数中，
#  这种成为“闭包”的程序结构拥有极大的威力。

# 当调用 lazy_sum() 时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2 # f1() 和 f2() 的调用结果互不影响

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量 args ，所以，
#  当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
#  所以，闭包用起来简单，实现起来不容易。

# 需要注意的问题是，返回的函数并没有立刻执行，而是直接调用了 f() 才执行。

def count():
    fs = []
    for i in xrange(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
# 每次循环，都创建了一个新的函数，然后，把创建的 3 个函数都返回了。
print f1()
print f2()
print f3()
# 全部都是 9 ，原因在于返回的函数应用了变量 i ，但它并非立刻执行。
#  等到 3 个函数都返回时，它们所引用的变量 i 已经变成了 3 ，因此最终结果为 9 。

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#  无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    fs = []
    for i in xrange(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

# 缺点是代码较长，可利用 lambda 函数缩短代码。
