#!/usr/bin python

result = ''

with open('enc', 'r') as fp:
	flag = fp.read()

for i in range(0, len(flag)):
	f = ord(flag[i]) >> 8
	result += chr(f)
	t = ((ord(flag[i])) - ((ord(flag[i]) >> 8) << 8))
	result += chr(t)
	print(result, flush=True)

