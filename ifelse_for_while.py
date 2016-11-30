#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = 3;
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# 非零数值 非空字符串 非空 list 判断为 True
x = ''
if x:
    print True
else:
    print False
print

# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
print

sum = 0
for x in xrange(101):
    sum += x
print '0 + 1 + ... + 100 =', sum

sum = 0
for x in xrange(1, 101):
    sum += x
print '1 + 2 + ... + 100 =', sum

sum = 0
for x in xrange(1, 100, 2):
    sum += x
print '1 + 3 + ... + 99  =', sum

sum = 0
for x in xrange(2, 101, 2):
    sum += x
print '2 + 4 + ... + 100 =', sum

print

# while
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print '99 + 97 + ... + 1 =', sum

# raw_input
# birth = raw_input('birth: ') # 永远返回字符串
birth = int(raw_input('birth: '))
print birth
if birth > 2000:
    print '00 后'
elif birth < 1900:
    print '90 前'
else:
    print '90 后'
