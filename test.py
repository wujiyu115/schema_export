# -*- coding: utf-8 -*-
# @Author: wujiyu115
# @Date:   2016-07-13 19:55:13
# @Last Modified by:   wujiyu115
# @Last Modified time: 2016-07-14 09:59:52


class D(object):
    """docstring for D"""
    def __init__(self, arg):
        super(D, self).__init__()
        self.arg = arg
d = D(1)

a = [1,2,3,4,5,6]
a.pop(3)
a.pop(0)
b = {}
b[d] = [22]
print(b)