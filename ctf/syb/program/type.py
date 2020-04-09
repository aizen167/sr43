# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 15:28
# @Author  :
# @Email   :
# @File    : type.py
# @Software: PyCharm

"""
聪明的打字员
"""

import Queue

target = 654321
ii = 0
num = [0, 0, 0, 0, 0, 0, 0]
a = [255 for x in range(0, 7000000)]  # 1123456-6999999 1123456->x654321
a[1123456] = 0
a[2123]
click = 0
s = Queue.Queue(maxsize=0)
s.put(click * 10000000 + 1123456)
while not s.empty() and click < 20:
    now = s.get()
    #print 'now', now
    click = now / 10000000 + 1
    i = now / 1000000 % 10
    num[1] = now / 100000 % 10
    num[2] = now / 10000 % 10
    num[3] = now / 1000 % 10
    num[4] = now / 100 % 10
    num[5] = now / 10 % 10
    num[6] = now % 10
    if i != 1:
        x = num[i]
        num[i] = num[1]
        num[1] = x
        temp = i * 1000000 + num[6] + num[5] * 10 + num[4] * \
            100 + num[3] * 1000 + num[2] * 10000 + num[1] * 100000
        if a[temp] > click:
            #print 'c',temp###
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
        x = num[1]
        num[1] = num[i]
        num[i] = x
    if i != 6:
        x = num[i]
        num[i] = num[6]
        num[6] = x
        temp = i * 1000000 + num[6] + num[5] * 10 + num[4] * \
            100 + num[3] * 1000 + num[2] * 10000 + num[1] * 100000
        if a[temp] > click:
            #print 'c',temp###
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
        x = num[6]
        num[6] = num[i]
        num[i] = x
    if i > 1:
        temp = (i - 1) * 1000000 + now % 1000000
        #print 'aa',a[temp],click
        if a[temp] > click:
            #print 'aaaaaa'
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
    if i < 6:
        temp = (i + 1) * 1000000 + now % 1000000
        if a[temp] > click:
            #print 'b',temp###
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
    if num[i] > 0:
        num[i] = num[i] - 1
        temp = i * 1000000 + num[6] + num[5] * 10 + num[4] * \
            100 + num[3] * 1000 + num[2] * 10000 + num[1] * 100000
        if a[temp] > click:
            #print 'c',temp###
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
        num[i] = num[i] + 1
    if num[i] < 9:
        num[i] = num[i] + 1
        temp = i * 1000000 + num[6] + num[5] * 10 + num[4] * \
            100 + num[3] * 1000 + num[2] * 10000 + num[1] * 100000
        if a[temp] > click:
            #print 'd',temp###
            a[temp] = click
            if temp % 1000000 == target:
                print click
            s.put(click * 10000000 + temp)
        num[i] = num[i] - 1
    #print 'click',click,'\n'
