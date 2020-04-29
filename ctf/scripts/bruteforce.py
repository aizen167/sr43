#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hashlib import md5
import string

strDic = string.printable
half_md5 = "1a4fb3fb5ee12307"
str = ""
for i1 in strDic:
	for i2 in strDic:
		for i3 in strDic:
			for i4 in strDic:
				str = i1 + i2 + i3 + i4 + "LiHua"
				strMd5 = md5(str.encode("utf-8")).hexdigest()
				if half_md5 in strMd5:
					print(str)
					exit(0)
print("done")
