#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile
import re
zipname = "/tmp/111111.zip"
while True:
	if zipname != "/tmp/73168.zip":
		ts1 = zipfile.ZipFile(zipname)
		print(ts1.namelist()[0])
		res = re.search('[0-9]*',ts1.namelist()[0])
		print(res.group())
		passwd = res.group()
		ts1.extractall("/tmp",pwd=passwd.encode())
		zipname = "/tmp/"+ts1.namelist()[0]
	else:
		print("find")

