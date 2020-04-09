# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 16:02
# @Author  :
# @Email   :
# @File    : blast.py
# @Software: PyCharm
"""
速度爆破
"""
import requests
from bs4 import BeautifulSoup
import threading
import hashlib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer': 'http://ctf5.shiyanbar.com/jia/index.php'}
rs = requests.Session()
url = r'http://ctf5.shiyanbar.com/ppc/sd.php'
a = rs.get(url, headers=headers).content.decode('utf-8')
soup = BeautifulSoup(a, "lxml")
d = soup.find_all(attrs={"name": "sha1"})
result = d[0].text
print(u'目标：' + result)


def jiami(a1, a2):
    global result
    for i in range(a1, a2):
        m1 = hashlib.md5(str(i).encode('utf-8')).hexdigest()
        m2 = hashlib.sha1(m1.encode('utf-8')).hexdigest()
        if (m2 == result):
            print('已找到')
            print(i)
            tijiao(str(i))


def tijiao(p_result):
    global url
    global rs
    global headers

    p_url = url
    postData = {'inputNumber': p_result, 'submit': '提交'}
    response = rs.post(p_url, data=postData, headers=headers)
    print(response.content.decode('utf-8'))
    print(response.status_code)
    exit()


t1 = threading.Thread(target=jiami, args=(0, 10001))
t2 = threading.Thread(target=jiami, args=(10001, 20001))
t3 = threading.Thread(target=jiami, args=(20001, 30001))
t4 = threading.Thread(target=jiami, args=(30001, 40001))
t5 = threading.Thread(target=jiami, args=(40001, 50001))

t6 = threading.Thread(target=jiami, args=(50001, 60001))
t7 = threading.Thread(target=jiami, args=(60001, 70001))
t8 = threading.Thread(target=jiami, args=(70001, 80001))
t9 = threading.Thread(target=jiami, args=(80001, 90001))
t10 = threading.Thread(target=jiami, args=(90001, 100001))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
