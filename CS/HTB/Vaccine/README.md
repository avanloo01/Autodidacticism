# Vaccine challenge

- started with an nmap scan

`nmap -sC -sV -T4 -oN nmap/initial IP`

- it showed an ftp, http & ssh

## FTP

- anonymous login was allowed
- I took the zip file
- using unzzip I could extract the files, but I couldn't see the contents
    - I used `zip2john` for the hash
- john easily cracked the hash
- I used 7z to extract the zip

## Source files

- a quick look at index.php shows us the password is hardcoded
    - as an md5
    - password: `qwerty789`

## HTTP

- we can login using the admin credentials
- there is just bland catalogue
- a search bar, but no XSS
- no LFI
- the tasks show I have to look into sqlmap
- ran gobuster, but I didn't really need to

### sqlmap

`sqlmap -u http://IP/dashboard.php --cookie="PHPSESSID=tbrf2sd9h9fcgrod4lmtnfp2op" --dump --os-shel --forms`

- This gave me a shell.
- I tried to establish a reverse shell with netcat, but it didn't work
- doing it again ...
    - works
- stabalizing shell
- trying to run `sudo -l`, but I don't know the password of postgres
    - in www/html: `P@s5w0rd!`

```bash
user.txt:ec9b13ca4d6229cd5cc1e09980965bf7
root.txt:dd6e058e814260bc70e9bbdef2715849
```

