import base64
s="UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==="
s=base64.b32decode(s)
m = ''
for i in s:
   x = ord(i) ^ 36
   x = x - 36
   m+= chr(x)
h = ''
for i in m:
   x = ord(i) - 25
   x = x ^ 36
   h+= chr(x)
print h
