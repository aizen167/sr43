# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 14:30
# @Author  :
# @Email   :
# @File    : joseph_circle.py
# @Software: PyCharm
"""
约瑟夫环
"""


def result(count, doom):
    length = 2 * count
    index = 0

    for i in range(count):
        index = (index + doom - 1) % length
        length -= 1
        if index < count:
            return False
    return True


k = 12
m = 1
while not result(k, m):
    m += 1
print(m)
