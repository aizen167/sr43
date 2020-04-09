import base64
import codecs
f = open(r'pic_png.txt').read()
fsave = open('pic.png', 'wb')
addHeader = '89 50 4E 47 0D 0A 1A 0A'.replace(' ', '')
a = codecs.decode(addHeader, 'hex')
fsave.write(a)
fsave.write(base64.b64decode(f))
fsave.close()
