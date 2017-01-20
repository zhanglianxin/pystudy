#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 序列化

try:
    import cPickle as pickle
except ImportError:
    import pickle

# pickle.dumps() 把任意对象序列化成一个 str
d = dict(name = 'Bob', age = 20, score = 88)
print pickle.dumps(d)
# pickle.dump() 把对象序列化后写入一个 file-like Object
f = open('./dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# pickle.load() 从一个 file-like Object 直接反序列化出对象
f = open('./dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d
print '---'

# JSON

# JSON 和 Python 内置的数据类型对应如下：
#  JSON 类型  Python 类型
#  {}         dict
#  []         list
#  "string"   'str' 或 u'unicode'
#  1234.56    int 或 float
#  true/false True/False
#  null       None

import json

# json.dumps() 把任意对象序列化成一个 str
d = dict(name = 'Bob', age = 20, score = 88)
print json.dumps(d)
# json.dump() 把对象序列化后写入一个 file-like Object
d = dict(name = 'Bob', age = 20, score = 88)
print json.dumps(d)
f = open('./dump.txt', 'wb')
json.dump(d, f)
f.close()
# json.loads() 把 JSON 的字符串反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str) # {u'age': 20, u'score': 88, u'name': u'Bob'}
# json.load() 从 file-like Object 读取字符串并反序列化
f = open('./dump.txt', 'rb')
d = json.load(f)
f.close()
print d
print '---'

# JSON 进阶
# 把对象实例序列化为 JSON
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# 转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)
print json.dumps(s, default = student2dict)
# 把任意 class 实例变为 dict
print json.dumps(s, default = lambda obj: obj.__dict__)
# 把 JSON 反序列化为对象实例
# 转换函数
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# loads() 方法首先转换出一个 dict 对象，
#  然后传入的 object_hook 函数负责把 dict 转换为 Student 实例
print json.loads(json_str, object_hook = dict2student)
# <__main__.Student object at 0x02754D50>
