#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单元测试
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value

import unittest

# 测试类，继承自 unittest.TestCase
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
# 单元测试 0
if __name__ == '__main__':
    unittest.main()
# 单元测试 1
# python -m unittest py_unittest.py

# setUp() setDown() 单元测试前/后执行
