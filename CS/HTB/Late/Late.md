# Late

> IP: 10.10.11.156

## Nmap

- Initial nmap shows ssh and http
- website for image tools
- there is a redirect to images.late.htb
	- adding it to /etc/hosts
- gobuster shows /assets, but I cannot access it
- XSS attempt in contact form doesn't work
- the dns server of images shows us an upload form
	- running Flask
- found a possible rev shell for Flask on GitHub
	- https://github.com/cyberhexe/flask-reverse-shell.git
	- it's for Windows
	= this doesn't seem to exist

## Writeup for help

- didn't think of just testing the OCR
- didn't know JS with double curly braces worked outside AngularJS
- didn't know SSTI
	- hacktricks.xyz is always good to check out
- Image to text doesn't work, so I'll just be following the writeup
- I didn't know pspy
- didn't know UID 0
- didn't know payloadallthethings
