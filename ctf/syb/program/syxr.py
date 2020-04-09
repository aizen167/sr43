# -*- coding:utf-8 -*-
#     祥9 瑞d[2] 生d[1] 辉d[0]
#  +  三1 羊0    献d[4] 瑞d[2]
# ------------------------------
# 三1 羊0 生d[1] 瑞d[2] 气d[3]
import random
# 随机0-9的数组


def shuzu():
    b1 = []
    while True:
        j = random.randint(2, 8)
        if j not in b1:
            b1.append(j)
        if(b1.__len__() == 5):
            break
    return b1
#


def shuzu1():
    while True:
        b2 = shuzu()
# "生"-"瑞"=1,瑞（2-7），生（3-8）
        if(b2[1] - b2[2] == 1 and b2[1] != 2 and b2[2] != 8):
            break
    print(b2)
    return b2


while True:
    # d生成随机的数组
    d = shuzu1()
# 祥c 瑞d[2] 生d[1] 辉d[0]
    xrsh = 9000 + d[2] * 100 + d[1] * 10 + d[0]
# 三a 羊b 献d[4] 瑞d[2]
    syxr = 1000 + d[4] * 10 + d[2]
# 三a 羊b生d[1] 瑞d[2] 气d[3]
    sxsrq = 10000 + d[1] * 100 + d[2] * 10 + d[3]
# 如果等式成立，就终止循环，输出数字
    if(sxsrq == xrsh + syxr):
        print("________________")
        print('  祥瑞生辉:', xrsh)
        print("+ 三羊献瑞:", syxr)
        print("三羊生瑞气:", sxsrq)
        break
