#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
    @author:    Alphabug@RedTeam.site
    @file:      crc32_number.py
    @time:      2020/3/14  22:42
"""
from zlib import crc32
def crc32_f(data):
    return hex(crc32(data.encode())&0xffffffff)[2:10]
def maker(length):
    n = 10 ** (length - 1)
    while True:
        print("[-]" ,n)
        n +=1
        if crc32_f(str(n)) == crc32_:
            print("[+] find it:",n)
            break
if __name__ == '__main__':
    length = int(input('length:'))
    crc32_ = input('crc32:').lower()
    maker(length)