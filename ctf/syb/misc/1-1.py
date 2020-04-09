import requests
import time

url = 'http://ctf5.shiyanbar.com/misc/keys/keys.php?key=1561358835'

s = requests.session()
while(1):
    res = s.get(url)
    print res.content
    if res.content.find('false') == -1:
        break
    time.sleep(1)
