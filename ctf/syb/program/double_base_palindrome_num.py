# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 14:39
# @Author  :
# @Email   :
# @File    : double_base_palindrome_num.py
# @Software: PyCharm
"""
双基回文数
"""


def trans_num(num, base):  # 进制转换
    num_list = []
    while(num):
        i = num % base
        num = num / base
        num_list.append(str(i))
    return ''.join(num_list[::-1])


def is_palindrome(num):  # 判断是否是双基回文数
    count = 0
    for i in range(2, 11):
        a = trans_num(num, i)
        if a == a[::-1]:
            count = count + 1
    if count >= 2:
        print num


for n in range(1600000, 1700000):
    is_palindrome(n)
