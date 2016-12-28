#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 形如 __xxx__ 的变量的特殊函数，可以定制类

# __str__() 返回用户看到的字符串
# __repr__() 返回开发者看到的字符串
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print Student('Michael')
Student('Michael') # FIXME not work

# __iter__ 返回一个迭代对象
class Fib(object):
    """docstring for Fib"""
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print n

# print Fib()[5] # 不能按下标访问

# __getitem__ 按照下标取得元素
class Fib(object):
    """docstring for Fib"""
    def __getitem__(self, n):
        a, b = 1, 1
        for x in xrange(n):
            a, b = b, a + b
        return a

# 按下标访问数列的任意一项
f = Fib()
print f[0]
print f[5]
print f[100]

print range(100)[5 : 10] # list 切片方法

# print f[0 : 5] # TypeError: an integer is required

class Fib(object):
    """docstring for Fib"""
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in xrange(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in xrange(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print f[0 : 5] # 取切片
print f[: 10]
print f[: 10 : 2]
# 还有与 __getitem__() 对应的方法， __setitem__(), __delitem__()
# 通过上面的方法，自定义的类表现得和 Python 自带的 list tuple dict
# 没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

# __getattr__ 动态返回一个属性
class Student(object):
    """docstring for Student"""
    def __init__(self):
        self.name = "Michael"        
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25 # 返回函数也是可以的
        # 只响应特定的几个属性，将其它抛出错误
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 当访问不存在的属性时，解释器会试图调用 __getattr__(self, 'score') 
#  来尝试获得属性。只有在未找到属性的情况下才会调用 __getattr_() 。
s = Student()
print s.name
print s.score
print s.age()
print s.abc # 访问其它不存在的属性返回 None
# 这实际上就把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？ 可以针对完全动态的情况作调用。

