# -*- coding: utf-8 -*-
# 模块
#如果是from导入的模块，可以通过起别名来避免冲突。
#***导入模块
#***动态带入模块
#动态导入
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
#***使用__future__
from __future__ import division

#兼容py 3.0的新功能
print 10/3
#***引用第三方模块
#①　easy_install
#②　pip｛推荐，已经内置到py2.7.9中，安装的时候选择pip｝
