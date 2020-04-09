import requests
import time
url = "http://ctf5.shiyanbar.com/misc/keys/keys.php"
key_time = int(time.time()) + 28800
url = "http://ctf5.shiyanbar.com/misc/keys/keys.php?key=" + str(key_time)
while True:
    print str(key_time)
    print str(int(time.time()))
    res = requests.get(url)
    print (res.text)
    if 'false' not in res.text:
        break
    time.sleep(1)
