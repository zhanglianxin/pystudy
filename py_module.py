#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 模块 Module
#  一个 .py 文件就是一个模块。
#  提高了代码的可维护性，还可以避免函数名和变量名冲突。

# 包 Package
#  避免模块名冲突，引入按目录来组织模块的方法。

# mycompany/
# |-- web/
#     |-- __init__.py # mycompany.web
#     |-- utils.py # mycompany.web.utils
#     |-- www.py # mycompany.web.www
# |-- __init__.py # mycompany
# |-- abc.py # mycompany.abc
# |-- utils.py # mycompany.utils
# |-- xyz.py # mycompany.xyz
