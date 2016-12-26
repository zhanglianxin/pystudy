#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @property 装饰器就是负责把一个方法变成属性调用的

class Student(object):
    """docstring for Student"""
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# 把一个 getter 方法变成属性，只需要加上 @property 就可以了，
#  此时， @property 本身又创建了另一个装饰器 @score.setter ，
#  负责把一个 setter 方法变成属性赋值，就拥有一个可控的属性操作。
s = Student()
s.score = 60
# s.score = 9999 # ValueError: score must between 0 ~ 100!

# 还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个只读属性：
class Student(object):
    """docstring for Student"""
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2016 - self._birth

s = Student()
s.birth = 1993
print s.age

# @property 广泛应用在类的定义中，可以让调用者写出简短的代码，
# 同时保证该参数进行必要的检查，程序运行时就减少了出错的可能性。
