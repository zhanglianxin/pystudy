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
