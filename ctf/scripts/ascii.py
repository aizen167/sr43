#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
ascii转换
"""
#str = 'cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'
#flag = ''

def dec2asc():
	number = [76,122,69,120,79,83,56,120,77,68,69,118,77,84,65,52,76,122,107,53,76,122,69,120,77,83,56,120,77,68,107,118,77,84,65,120,76,122,69,120,78,105,56,120,77,84,69,118,79,84,99,118,77,84,69,50,76,122,69,120,78,105,56,53,78,121,56,53,79,83,56,120,77,68,99,118,79,84,99,118,77,84,69,119,76,122,69,119,77,67,56,120,77,68,65,118,77,84,65,120,76,122,69,119,77,105,56,120,77,68,69,118,77,84,69,119,76,122,107,53,76,122,69,119,77,83,56,120,77,84,107,118,77,84,69,120,76,122,69,120,78,67,56,120,77,68,103,118,77,84,65,119]
	#number = [119,101,108,99,111,109,101,116,111,97,116,116,97,99,107,97,110,100,100,101,102,101,110,99,101,119,111,114,108,100]
	for i in number:
		flag += chr(i)
	print(flag)

def hex2asc():
	#str = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"
	#str = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd"
	str = "666c61677b68656c6c6f5f776f726c647d"
	flag = ''
	for i in range(0,len(str),2):
		s = "0x" + str[i] + str[i+1]
		flag += chr(int(s, 16) -0)
	print(flag)

#for i in range(0, len(str)):
#    print(ord(str[i]))

#for i in range(3, len(str), 5):
#    flag += str[i]
 
def oct2asc():
	number = [0126,062,0126,0163,0142,0103,0102,0153,0142,062,065,0154,0111,0121,0157,0113,0111,0105,0132,0163,0131,0127,0143,066,0111,0105,0154,0124,0121,060,0116,067,0124,0152,0102,0146,0115,0107,065,0154,0130,062,0116,0150,0142,0154,071,0172,0144,0104,0102,0167,0130,063,0153,0167,0144,0130,060,0113]
	for i in number:
		flag += chr(int(i))
	print(flag)

hex2asc()
