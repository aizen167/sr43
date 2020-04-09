# -*- coding: utf8 -*-

def revStr(s):
	news=""
	for i in xrange(0,len(s),4):
		news+=s[i+2:i+4]
		news+=s[i:i+2]
	return news

def foo():
	f=open('funfile')
	s="377a" #7z的意思
	for line in f:
		s+=revStr(line.strip()[8:].replace(' ',''))
	fsave=open('funsave.7z','wb') #必须有个b
	fsave.write(s.decode('hex'))
	fsave.close()
	pass

if __name__ == '__main__':
	foo()
	print 'ok'
