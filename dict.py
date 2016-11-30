#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dictionary 字典 使用键值对存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d
print d['Michael']

# 存储数据，除了初始化指定，还可以通过 key 放入
d['Adam'] = 67
print d
print d['Adam']

# 键是唯一的，且按字典顺序排序
# 键不存在，就会报错
# print d['Thomas']
# 避免 keyError
#   1. in 判断是否存在
print 'Thomas' in d # False
#   2. 通过 get() 方法，返回 None 或者指定 value
print d.get('Thomas') # None
print d.get('Thomas', -1) # -1

# 删除 key 返回该键对应的值
print d.pop('Bob') # 75

# dict 特点
#  1. 查找和插入的速度极快，不会随着 key 的增加而增加
#  2. 需要占用大量的内存，内存浪费多
# 和 list 相比，是用空间来换取时间的一种方法

# dict 的 key 必须是 **不可变对象**
# list 是可变的，不能作为 key
