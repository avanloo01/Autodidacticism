#!/usr/bin python

result = ''
flag = 'brrr'

for i in range(0, len(flag), 2):
	firstChar = chr((ord(flag[i]) << 8)) 
	secondChar = chr(ord(flag[i+1]))
	result += firstChar + secondChar

print(result)
