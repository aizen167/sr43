# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 14:52
# @Author  :
# @Email   :
# @File    : brackets.py
# @Software: PyCharm

"""
括号表达式
"""
num = [4, 6, 6, 6, 6, 8, 9, 9, 9]
s = 0
str = ''
for x in range(0, 9):
    str = str + '(' * (num[x] - s) + ')'
    s = num[x]
print str
index = 0
ans = ''
for i in range(0, 9):
    index = str.find(')', index)
    c = 1
    count = 0
    for j in range(1, index + 1):
        if str[index - j] == '(':
            count = count + 1
            c = c - 1
        else:
            c = c + 1
        if c == 0:
            break
    count = bytes(count)
    index = index + 1
    ans = ans + count
print 'CTF{' + ans + '}'
