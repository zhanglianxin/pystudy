#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 偏函数 

# functools.partial 的作用：
#  把一个函数的某些参数给固定住（也就是设置默认值），
#  返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int, base = 2)
print int2('1000000')
# 上面的新的 int2 函数，仅仅是把 base 参数重新设定
#  默认值为 2 ，也可以在函数调用时传入其他值
print int2('1000000', base = 10)

# 创建偏函数时，可以接收函数对象、 *args 和 **kw 这 3 个参数，
#  当传入 int2 = functools.partial(int, base = 2)
#  实际上固定了 int() 函数的关键字参数 base ，也就是：
#  int2('10010')
#  相当于：
#  kw = {base: 2}
#  int('10010', **kw)

#  当传入：
max2 = functools.partial(max, 10)
#  实际上会把 10 作为 *args 的一部分自动加到左边，也就是：
max2(5, 6, 7)
#  相当于：
args = (10, 5, 6, 7)
print max(*args)

# 当参数的个数太多需要简化时，使用 functools.partial 创建一个偏函数，
#  这个新函数可以固定住原函数的部分函数，从而在调用时更简单。
