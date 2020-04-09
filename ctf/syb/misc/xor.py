# -*- coding: utf8 -*-
m1 = open("密文.txt", "rb").read()
m2 = open("明文.txt", "rb").read()
message = "".join(map(lambda item: chr(ord(item[0]) ^ ord(item[1])), zip(m1, m2)))
print message
