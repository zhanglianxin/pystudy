#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 安装和使用第三方模块

# [pip install PIL fails](http://stackoverflow.com/questions/32772596/pip-install-pil-fails)
from PIL import Image
im = Image.open('test.jpg')
print im.format, im.size, im.mode # JPEG (960, 1276) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 模块搜索路径

# 默认情况下，解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
#  搜索路径存放在 sys 模块的 path 变量中
# 如果添加自己的搜索目录，有两种方法：
# 1. 直接修改 sys.path ，添加要搜索的目录，这种方法是在运行时修改，运行结束后失效
# import sys
# sys.path.append('path')
# 2. 设置环境变量 PYTHONPATH ，该环境变量的内容会被自动添加到模块搜索路径中。
#    只需要添加自己的搜索路径，Python 本身的搜索路径不受影响。
