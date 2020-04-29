#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PIL.Image as Image

"""
lsb隐写
"""

img = Image.open('low.bmp')
img_tmp = img.copy()
pix = img_tmp.load()
width,height = img_tmp.size
for w in range(width):
    for h in range(height):
        if pix[w,h]&1 == 0:
            pix[w,h] = 255
        else:
            pix[w,h] = 0
img_tmp.save('flag.bmp')
