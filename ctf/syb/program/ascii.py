# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 15:18
# @Author  :
# @Email   :
# @File    : ascii.py
# @Software: PyCharm
"""
ASCII艺术
"""
import requests
from bs4 import BeautifulSoup as BS

sess = requests.Session()

CHARS = [
    # 0
    [' xxx ',
     'x   x',
     'x   x',
     'x   x',
     ' xxx '],
    # 1
    [' xx',
        '  x x  ',
        '  x  ',
        '  x  ',
        'xxxxx'],
    # 2
    [' xxx ',
     'x   x ',
     '  xx ',
     ' x   ',
     'xxxxx'],
    [], [],
    # 5
    ['xxxxx',
     'x    ',
     ' xxxx',
     '    x',
     'xxxxx'],
    [], [],
    # 8
    [' xxx ',
     'x   x',
     '  xx ',
     'x   x',
     ' xxx '],
    # 9
    [' x   x',
     'x    x',
     ' xxxxx',
     '     x',
     '    x']
]

chars = BS(sess.get('http://ctf5.shiyanbar.com/ppc/acsii.php').text,
           'lxml').select_one('div[name=sha1]')
chars = [s.replace(u'\xa0', ' ') for s in chars.strings]

result = [CHARS.index(chars[i:i + 5]) for i in range(0, len(chars), 5)]
resp = sess.post('http://ctf5.shiyanbar.com/ppc/acsii.php',
                 data={'inputNumber': ''.join(map(str, result))}).text
print(resp)
