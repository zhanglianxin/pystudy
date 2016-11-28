#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串
print ord('A') # 获取单个字符的整数表示
print chr(66) # 把编码转换为对应的字符
# print u'中文'
print '---'

# Unicode -> UTF-8
print u'ABC'.encode('utf-8') # ABC
print u'中文'.encode('utf-8') # 中文 \xe4\xb8\xad\xe6\x96\x87
# UTF-8 -> Unicode
print 'ABC'.decode('utf-8') # ABC
# print '中文'.decode('utf-8') # 中文
print '---'

# 返回字符串的长度
print len(u'ABC') # 3
print len('ABC') # 3
print len(u'中文') # 2
print len('中文') # 6
print '---'

# 格式化
print 'Hello, %s' % 'python'
print 'Hi, %s, u have $%d.' % ('Michael', 100000000)

# 常见的占位符：
#   %d 整数
#   %f 浮点数
#   %s 字符串
#   %x 十六进制整数

print '%2d-%02d' % (3, 1) # ' 3-01'
print '%.2f' % 3.1415926 # 3.14

# %s 会把任何数据类型转换为字符串
print 'Age: %s, Gender: %s' % (25, True)

print u'Hi, %s' % u'Michael'
print u'Hi, %s' % u'米歇尔'

# 对 % 进行转义
print 'growth rate: %d %%' % 7
