# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 15:14
# @Author  :
# @Email   :
# @File    : split.py.py
# @Software: PyCharm
"""
分数拆分
"""
count = 0
num_list = []
for y in range(201, 600):
    if (400 * y) % (y - 200) == 0:
        count = count + 1
        str_add = str((400 * y) / (y - 200)) + ':' + str(y)
        num_list.append(str_add)

print 'count=' + str(count)
print num_list
