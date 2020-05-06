#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import binascii
import os

png_file = "/tmp/tmp.png"
m = open(png_file, "rb").read()
for i in range(1024):
	c = m[12:16] + struct.pack('>i', i) + m[20:29]
	crc = binascii.crc32(c) & 0xffffffff
	if crc == 0x932f8a6b:
		print(i)
