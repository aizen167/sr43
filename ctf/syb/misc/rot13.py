import hashlib


def result(asci):
    for i in asci:
        for j in asci:
            for m in asci:
                for n in asci:
                    md = hashlib.md5(
                        ('flag{www_shiyanbar_com_is_very_good_' +
                         chr(i) +
                            chr(j) +
                            chr(m) +
                            chr(n) +
                            '}').encode('utf-8')).hexdigest()
                    print(chr(i) + chr(j) + chr(m) + chr(n))
                    if md == md5_test:
                        return md, chr(i) + chr(j) + chr(m) + chr(n)
    return 0, 0


lst = [
    83,
    89,
    78,
    84,
    45,
    86,
    96,
    45,
    115,
    121,
    110,
    116,
    136,
    132,
    132,
    132,
    108,
    128,
    117,
    118,
    134,
    110,
    123,
    111,
    110,
    127,
    108,
    112,
    124,
    122,
    108,
    118,
    128,
    108,
    131,
    114,
    127,
    134,
    108,
    116,
    124,
    124,
    113,
    108,
    76,
    76,
    76,
    76,
    138,
    23,
    90,
    81,
    66,
    71,
    64,
    69,
    114,
    65,
    112,
    64,
    66,
    63,
    69,
    61,
    70,
    114,
    62,
    66,
    61,
    62,
    69,
    67,
    70,
    63,
    61,
    110,
    110,
    112,
    64,
    68,
    62,
    70,
    61,
    112,
    111,
    112]
lst = [chr(i - 13) for i in lst]
flag = "".join(lst)
md5_test = '38e4c352809e150186920aac37190cbc'

asci = [i for i in range(33, 127)]
md, ch = result(asci)
print('md=', md)
print('ch=', ch)
