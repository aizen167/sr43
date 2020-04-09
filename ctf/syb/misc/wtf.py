# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 13:46
# @Author  :
# @Email   :
# @File    : wtf.py
# @Software: PyCharm
from PIL import Image

im=Image.new('RGB',(256,256))
pix = im.load()
with open('code.txt') as f:
    txt=f.read()
    for x in xrange(len(txt)):
        if txt[x] == '1':
            pix[x/256,x%256]=(0,0,0)
        else:
            pix[x/256,x%256]=(255,255,255)
im.save('1.png')
