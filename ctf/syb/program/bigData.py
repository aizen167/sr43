# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 15:10
# @Author  :
# @Email   :
# @File    : bigData.py
# @Software: PyCharm
"""
大数据问题
"""
s = 0
j = 1
for x in range(1, 6790):
    j *= x  # j是用来求阶乘和的，每下一个阶乘和都可以用到上一个阶乘和
    s = (s + j) % 100000
print(s)
