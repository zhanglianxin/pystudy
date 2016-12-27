#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mixin 给一个类增加多个功能
# 设计类的时候，优先考虑通过多重继承来组合多个 Mixin 的功能，
#  而不是设计多层次的复杂的继承关系。

# 编写一个多进程模式的 TCP 服务
def MyTCPServer(TCPServer, ForkingMixin):
    pass
# 编写一个多进程模式的 UDP 服务
def MyUDPServer(UDPServer, ThreadingMixin):
    pass
# 编写一个更先进的协程模型
def MyTCPServer(TCPServer, CoroutineMixin):
    pass
# 不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类

# 由于 Python 允许使用多重继承，因此， Mixin 就是一种常见的设计。
# 只允许单一继承的语言 (e.g. Java) 不能使用 Mixin 的设计。
