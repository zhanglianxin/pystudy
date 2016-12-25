#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 访问限制

# 在类内部，可以有属性和方法，而外部代码可以通过直接调用
#  实例变量的方法来操作数据，这样就隐藏了内部的复杂逻辑。

# 如果要让内部属性不被外部访问，可以把属性的名称前加上 __ ，
# 在 Python 中，实例的变量名如果以 __ 开头，就变成了一个私有变量，
#  只有内部可以访问，外部不能访问。

class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self, name):
        self.__name = name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

bart = Student('Bart Simpson', 98)
# print bart.__name # AttributeError: 'Student' object has no attribute '__name'
# 这样就确保了外部代码不能随意修改对象内部的状态，通过访问限制的保护，代码更加健壮。

# 以双下划线开头、并且以双下划线结尾的是特殊变量，可以直接访问，不是 private 变量

# 以一个下划线开头的实例变量名，这样的实例变量外部是可以访问的，
#  但是按照约定俗成的规定，当看到这样的变量时，意思是：
#  虽然可以被访问，但是请视为私有变量，不要随意访问。

# 双下划线开头的实例变量不是一定不能从外部访问的。
# 不能直接访问 __name 是因为 Python 解释器对外把 __name 变量改成了
#  _Student__name ，所以仍然可以通过 _Student__name 来访问 __name 变量。

bart1 = Student('Bart1 Simpson', 99)
bart.print_score()
bart1.print_score()

bart1._Student__score = 0 # 修改实例变量

bart.print_score()
bart1.print_score()
