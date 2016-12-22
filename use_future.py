#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __future__ 模块
# 把新版本的特性导入到当前版本，测试新版本的一些特性

# still running on Python 2.7

from __future__ import unicode_literals, division

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
print '\n'

# from __future__ import division

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3
