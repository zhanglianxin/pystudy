#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用模块

'a test module' # 模块的文档注释
# 任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'zhanglianxin'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'
if __name__ == '__main__':
    test()

# 别名
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到 ImportError
    import StringIO

# 作用域

# 限制函数和变量仅在模块内部使用，不应该被直接引用

def _private_1(name):
    return 'Hello, %s' % name
def _private_2(name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 在模块里公开 greeting() 函数，而把内部逻辑用 private 函数隐藏起来，
#  这样，调用 greeting() 函数不用关心内部的 private 函数细节，
#  这也是一种非常有用的代码封装和抽象的方法
# 即：外部不需要引用的函数全部定义成 private ，
#  只有外部需要引用的函数才定义为 public
