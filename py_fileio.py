#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文件读写

# 读文件
try:
    f = open('./.gitignore', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('./.gitignore', 'r') as f:
    print f.read()
    # print f.read(size) # 读取指定大小
    # print r.readline() # 读取一行内容
    # print r.readlines() # 读取所有内容按行返回 list （配置文件）
    for line in f.readlines():
        print(line.strip()) # 把末尾的 '\n' 删掉

# file-like Object
# 像 open() 函数返回的这种有个 read() 方法的对象，在 Python 中
#  统称为 file-like Object 。除了 file 外，还可以是内存的字节流、
#  网络流、自定义流等等。 file-like Object 不要求从特定类继承，
#  只要写个 read() 方法就行。
#  StringIO 就是内存中创建的 file-like Object ，常用作临时缓冲。

# 二进制文件
#  用 'rb' 模式打开文件
f = open('./thumb.jpg', 'rb')
print f.read()

# 字符编码
#  要读取非 ASCII 编码的文件，就必须以二进制模式打开，再编码
f = open('./.gitignore', 'rb')
u = f.read().decode('gbk')
print u

# codecs 模块帮助在读文件时自动转换编码，直接读出 unicode
import codecs
with codecs.open('./.gitignore', 'r', 'gbk') as f:
    print f.read()

# 写文件
f = open('./py_write.txt', 'w')
f.write('Hello, python!')
f.close()

with open('./py_write.txt', 'w') as f:
    f.write('Hello, python!')
