# Meta

## Nmap

- ssh: Debian
- artcorp server

## VHOST enum

- dev01.artcorp.htb
    - links to metaview
        - uploads
        - only jpg & png
        - trying valid jpg
            - outputs exiftool

## Metaview app

- php app

## File upload

- adding php code in comment $\implies$ XSS

## XSS

- using php tags that don't show up
- bold tags

## Public exploits for exiftool

## Malicious image w/ CVE-2021-22204

- setting up a rev shell text on a simple server
    - no curl
    - wget does
        - with -O (output) - (stdout)


## Rev shell

- `python3 -c 'import pty;pty.spawn("/bin/bash")'`
- ^Z
- `stty raw -echo; fg`
- `export TERM=xterm`
- `stty -a`
- `rows 26 cols 105`


## Convert_images dir

- used to pass images to exiftool
- found script w/ `grep -R convert_images / 2>/dev/null`
- look at mogrify
    - imagemagick cves
        - all to old

## convert_images script

## CVE-2020-29599

- pwn.svg
- 

## neofetch w/ sudo

- using shell again to user Thomas
- gtfobin
- env_keep $\implies$ persists through sudo (found w/ `sudo -l`)
- export XDG_CONFIG_HOME to /home/thomas/.config
- add gtfobin in neofetch config
