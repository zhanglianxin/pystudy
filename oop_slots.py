#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __slots__ 限制本类允许定义的属性

class Student(object):
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print s.name, s.age

# 给一个实例绑定一个方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age(25)
# print s2.name, s2.age # AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例都绑定方法，可以给类绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)
# 给类绑定方法后，所有实例均可调用：
s.set_score(100)
print s.score
s2.set_score(99)
print s2.score
# 通常情况下，set_score() 方法可以直接定义在类中，
# 但动态绑定允许在程序的运行过程中动态给类加上功能，这在静态语言中很难实现。

# 为了达到限制的目的， Python 允许在定义类的时候，定义一个特殊的
#  __slots__ 变量，来限制该类能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用 tuple 定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# AttributeError: 'Student' object has no attribute 'score'
# s.score = 99
# 由于 score 没有被放到 __slots__ 变量中，所以不能绑定 score 属性，
#  试图绑定 score 将得到 AttributeError 的错误。

# 使用 __slots__ 定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999

# 除非在子类中也定义 __slots__ ，这样，子类允许定义的属性就是
#  自身的 __slots__ 加上父类的 __slots__
