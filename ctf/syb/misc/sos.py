#!/usr/bin/env python3
# -*- coding:utf8 -*-
import gzip

def foo():
    path = r"/mnt/%d"
    s = ""
    for i in range(1, 242 + 1):
        with open(path % i, 'rb') as f:
            s += gzip.decompress(f.read()).decode()
    print (s)
    pass


if __name__ == '__main__':
    foo()
    print ('ok')
