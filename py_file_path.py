#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 操作文件和目录

import os
# 操作系统名字
print os.name # nt
# 详细的系统信息
# print os.uname() # 此函数在 Windows 上不提供

# 环境变量
print os.environ
# 某个环境变量的值
print os.getenv('path')

# 操作文件和目录
# 查看当前目录的绝对路径
print os.path.abspath('.')
# 在某个目录下创建一个新目录
#  首先把新目录的完整路径表示出来：
newdir = os.path.join(os.path.abspath('.'), 'testdir')
print newdir # 输出新目录的绝对路径
#  创建目录
os.mkdir(newdir)
#  删除目录
os.rmdir(newdir)
# 把两个路径合并成一个时，不要直接拼接字符串，而是通过 os.path.join() 函数，
#  这样可以正确处理不同操作系统的路径分隔符。
# 同理，要拆分路径时，也不要直接去拆字符串，而是通过 os.path.split() 函数，
#  这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.split(os.path.abspath('./.gitignore'))
# 文件扩展名
print os.path.splitext(os.path.abspath('./.gitignore'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 文件操作
# 对文件重命名
# 先创建文件，否则报错
with open('./py_write.txt', 'w') as f:
    f.write('Hello, python!')
os.rename('./py_write.txt', './py_write.py')
# 复制文件
import shutil
shutil.copyfile('./py_write.py', './py_write1.py')
# 删除文件
os.remove('./py_write.py')
os.remove('./py_write1.py')
# 过滤文件
# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的 .py 文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print '---'

# TODO 编写一个 search(s) 的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
def search(s):
    pass
    
search('py')
