#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类和实例

# 所有类最终都会继承自 object 类
class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print '%s: %s' % (self.name, self.score)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print bart # <__main__.Student object at 0x01D2E6B0>
print Student # <class '__main__.Student'>
# __init__ 方法的第一个参数永远是 self ，表示创建的实例本身，因此在方法内部，
#  可以把各种属性绑定到 self ，因为 self 就指向创建的实例本身。
#  在创建实例时不能传入空参数，必须传入与 __init__ 方法匹配的参数。
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是
#  实例变量 self ，并且调用时不用传递该参数。除此之外，类的方法和普通函数
#  没有什么区别，仍然可以使用默认参数、可变参数和关键字参数。

# 数据封装

print bart.get_grade()

# 类是创建实例的模板，而实例则是一个一个具体的对象，
#  各个实例拥有的数据都互相独立，互不影响；
#  方法就是与实例绑定的函数，和普通函数不同，
#  方法可以直接访问实例的数据；通过在实例上调用方法，
#  就直接操作了对象内部的数据，无需知道方法内部的实现细节。
# 和静态语言不同，Python 允许对实例变量绑定任何数据，
# 也就是说，对于两个实例变量，虽然它们都是一个类的不同实例，
#  但拥有的变量名称都可能不同：

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print bart.age
print lisa.age # AttributeError: 'Student' object has no attribute 'age'
