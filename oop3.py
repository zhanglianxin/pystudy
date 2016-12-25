#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 继承和多态

class Animal(object):
    """docstring for Animal"""
    def run(self):
        print 'Animal is running...'
class Dog(Animal):
    """docstring for Dog"""
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
class Cat(Animal):
    """docstring for Cat"""
    def run(self):
        print 'Cat is running...'

# 继承：子类获得了父类的全部功能。

dog = Dog()
dog.run()
cat = Cat()
cat.run()

print isinstance(dog, Dog)
print isinstance(cat, Cat)
print isinstance(dog, Animal)
print isinstance(cat, Animal)

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    """docstring for Tortoise"""
    def run(self):
        print 'Tortoise is running slowly...'

run_twice(Tortoise())

# 多态：传入任意类型，只要是父类或者子类，就会自动调用实际类型的具体方法。
# 调用方只管调用，不管细节。开闭原则：对扩展开放，对修改封闭。

# 继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，
#  子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 有了继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，
#  这样，所有子类类型都可以正常被接收；
# 任何时候，如果没有合适的类可以继承，就继承自 object 类。
