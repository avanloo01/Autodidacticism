# Driver

## nmap

- http (IIS $\implies$Win)
    - Multi functional printer
- 135, 445 $\implies$ smb

## SMB, CME for hostname

- smbclient -L //IP
-U ''
-N
...
- hostname: DRIVER

## Website, admin:admin, gobuster

- upload form
- gobuster: -U admin -P admin -x php

## SCF Files to steal NTLMv2 Hashes

- Shell Command Files
    - allows icons $\implies$ shell
- attack.scf
- using responder.py
    - retrieves hash for usr tony

## hashcat

- first run it with just a wordlist
- using -m to show version

## CME 

## Evil-WinRM

## Ricoh printer driver

## Ricoh printer driver exploit

## Issue w/ WinRM Module in MSF

## MSFVenom for executable & meterpreter shell

## 32 bit payload

## Exploit works

## PrintNightmare to privesc

- upload powershell script; upload on evil-winrm
    - immediately shows function

## 2 WinRM MSF Scripts

- 
