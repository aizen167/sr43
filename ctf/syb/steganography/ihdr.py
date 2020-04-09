# -*- coding:utf-8 -*-

import binascii
def crc32(v):
	return '%x' % (binascii.crc32(v) & 0xffffffff) 

def foo():
	chunk_type="49484452"
	chunk_data="0000029C 000001DD 08 06 00 00 00"
	chunk_crc="FE1A5AB6"
	print "Old:",chunk_crc
	chunk_crc=(chunk_type+chunk_data).replace(' ','').decode('hex')
	print "New:",crc32(chunk_crc).upper()
	pass

if __name__ == '__main__':
	foo()
	print 'ok'
