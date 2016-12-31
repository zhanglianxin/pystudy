#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用元类

# type() 查看一个类型或变量的类型
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
from hello import Hello

h = Hello()
h.hello() # Hello, world
print(type(Hello)) # <type 'type'> 类的类型
print(type(h)) # <class 'hello.Hello'> 实例的类型

# type() 函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name = 'world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object, ), dict(hello = fn)) # 创建 Hello 类
h = Hello()
h.hello() # Hello, world.
print(type(Hello)) # <type 'type'>
print(type(h)) # <class '__main__.Hello'>

# 要创建一个类对象， type() 函数依次传入 3 个参数：
#  1. 类的名称；
#  2. 继承的父类集合；
#  3. 类的方法名称与函数绑定。
# 通过 type() 函数创建的类和直接写类是完全一样的，因为 Python 解释器
# 遇到类定义时，仅仅是扫描一下类定义的语法，然后调用 type() 函数创建出类。

# metaclass 元类 允许创建类或修改类，可以把类看成是元类创建出来的“实例”。
# metaclass 是创建类，所以必须从 type 类型派生
class ListMetaclass(type):
    """docstring for ListMetaclass"""
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用 ListMetaclass 来定制类

# __new__() 方法接收到的参数依次是：
#  1. 当前准备创建的类的对象；
#  2. 类的名字；
#  3. 类继承的父类集合；
#  4. 类的方法集合。

L = MyList()
L.add(1) # 普通的 list 没有 add() 方法
print L # [1] 

# 动态修改有什么意义？
# 要编写一个 ORM 框架，所有的类都只能动态定义，
#  因为只有使用者才能根据表的结构定义出对应的类来。

# TODO make an ORM framework
