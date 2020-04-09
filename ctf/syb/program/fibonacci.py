# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 15:14
# @Author  :
# @Email   :
# @File    : fibonacci.py
# @Software: PyCharm
"""
斐波那契数列
"""

def fibs(n):
    result = [1, 1, 1]
    if n >= 3:
        for i in range(3, n + 1):
            result.append(result[i - 3] + result[i - 2] + result[i - 1])
    return result[n]


if __name__ == '__main__':
    print str(fibs(99))[0:8]
    print 'ok'
