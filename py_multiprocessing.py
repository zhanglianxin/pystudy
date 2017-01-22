#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 多进程

# fork() 函数调用一次，返回两次。（Windows 没有 fork 调用）
# 子进程返回 0 ，父进程返回子进程的 ID 。一个父进程可以 fork 出很多子进程。
# 父进程要记下每个子进程的 ID ，而子进程只需要调用 getppid() 就可以拿到父进程的 ID 。
# import os

# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid == 0:
#     print 'I am child process (%s) and my parent is %s' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# 有了 fork 调用，一个进程在接到新任务时就可以复制出一个子进程来处理任务。
#  常见的 Apache 服务器就是由父进程监听端口，每当有新的 http 请求时，
#  就 fork 出子进程来处理新的 http 请求。

# multiprocessing 模块提供了一个 Process 类来代表一个进程对象。
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target = run_proc, args = ('test',))
    print 'Process will start.'
    p.start()
    p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print 'Process end.'

# TODO uncompleted
