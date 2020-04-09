mask_in = open('masked_key.png','rb')
key = bytearray(mask_in.read(983040-64))
mask= bytearray(mask_in.read(64))
for x in range(983040-64):
    key[x] ^= mask[x%64]
key_out = open('unmasked_key.png','wb')
key_out.write(key)
key_out.close()
