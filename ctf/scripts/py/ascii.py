#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
ascii转换
"""


#str = 'cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}'
#flag = ''


def dec2asc():
    flag = ""
    number = [
        76,
        122,
        69,
        120,
        79,
        83,
        56,
        120,
        77,
        68,
        69,
        118,
        77,
        84,
        65,
        52,
        76,
        122,
        107,
        53,
        76,
        122,
        69,
        120,
        77,
        83,
        56,
        120,
        77,
        68,
        107,
        118,
        77,
        84,
        65,
        120,
        76,
        122,
        69,
        120,
        78,
        105,
        56,
        120,
        77,
        84,
        69,
        118,
        79,
        84,
        99,
        118,
        77,
        84,
        69,
        50,
        76,
        122,
        69,
        120,
        78,
        105,
        56,
        53,
        78,
        121,
        56,
        53,
        79,
        83,
        56,
        120,
        77,
        68,
        99,
        118,
        79,
        84,
        99,
        118,
        77,
        84,
        69,
        119,
        76,
        122,
        69,
        119,
        77,
        67,
        56,
        120,
        77,
        68,
        65,
        118,
        77,
        84,
        65,
        120,
        76,
        122,
        69,
        119,
        77,
        105,
        56,
        120,
        77,
        68,
        69,
        118,
        77,
        84,
        69,
        119,
        76,
        122,
        107,
        53,
        76,
        122,
        69,
        119,
        77,
        83,
        56,
        120,
        77,
        84,
        107,
        118,
        77,
        84,
        69,
        120,
        76,
        122,
        69,
        120,
        78,
        67,
        56,
        120,
        77,
        68,
        103,
        118,
        77,
        84,
        65,
        119]
    # number = [119,101,108,99,111,109,101,116,111,97,116,116,97,99,107,97,110,100,100,101,102,101,110,99,101,119,111,114,108,100]
    for i in number:
        flag += chr(i)
    print(flag)


def hex2asc():
    # str = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"
    # str = "d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1e6b3e3b9e4b3b7b7e2b6b1e4b2b6b9e2b1b1b3b3b7e6b3b3b0e3b9b3b5e6fd"
    str = "666c61677b68656c6c6f5f776f726c647d"
    flag = ''
    for i in range(0, len(str), 2):
        s = "0x" + str[i] + str[i + 1]
        flag += chr(int(s, 16) - 0)
    print(flag)


# for i in range(0, len(str)):
#    print(ord(str[i]))


def bin2str():
    str1 = "110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101"
    flag = ""
    for i in range(0, len(str1), 7):
        flag += chr(int('0' + str1[i:i + 7], 2))
    print(flag)


def oct2asc():
    flag = ""
    number = [
        0o126,
        0o62,
        0o126,
        0o163,
        0o142,
        0o103,
        0o102,
        0o153,
        0o142,
        0o62,
        0o65,
        0o154,
        0o111,
        0o121,
        0o157,
        0o113,
        0o111,
        0o105,
        0o132,
        0o163,
        0o131,
        0o127,
        0o143,
        0o66,
        0o111,
        0o105,
        0o154,
        0o124,
        0o121,
        0o60,
        0o116,
        0o67,
        0o124,
        0o152,
        0o102,
        0o146,
        0o115,
        0o107,
        0o65,
        0o154,
        0o130,
        0o62,
        0o116,
        0o150,
        0o142,
        0o154,
        0o71,
        0o172,
        0o144,
        0o104,
        0o102,
        0o167,
        0o130,
        0o63,
        0o153,
        0o167,
        0o144,
        0o130,
        0o60,
        0o113]
    for i in number:
        flag += chr(int(i))
    print(flag)


if __name__ == '__main__':
    bin2str()
