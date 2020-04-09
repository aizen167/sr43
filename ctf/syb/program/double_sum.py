# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 15:01
# @Author  :
# @Email   :
# @File    : double_sum.py
# @Software: PyCharm
"""
两个最大子串和
"""


def foo():
    # 读取文件
    f = open('data.txt').read().replace("\n", '')
    lst = list(eval(f))  # 150项

    # 正向记录每一项的max
    max, sum = 0, 0
    lst1 = []
    for i in xrange(len(lst)):
        if sum >= 0:
            sum += lst[i]
        else:
            sum = lst[i]
        if max < sum:
            max = sum
        lst1.append(max)

    # 逆向记录每一项的max
    max, sum = 0, 0
    lst2 = []
    for i in xrange(len(lst) - 1, -1, -1):
        if sum >= 0:
            sum += lst[i]
        else:
            sum = lst[i]
        if max < sum:
            max = sum
        lst2.append(max)
    # 倒置下
    lst2 = lst2[::-1]

    # 计算两个子串的最大和的和
    max, sum = 0, 0
    for i in xrange(len(lst1) - 1):
        # 因为lst2是降序排列的，所以这里只需要判断到i+1
        sum = lst1[i] + lst2[i + 1]
        if max < sum:
            max = sum

    print max
    pass


if __name__ == '__main__':
    foo()
    print 'ok'
    pass
