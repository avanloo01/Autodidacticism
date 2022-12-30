# Information Stealer, malware analysis

- list files in powershell directory

## Original.cmd

- calls powershell 
- windowstyle hidden
- execution policy: bypass
- runs script
    - long file name
    - powershell: ps1

## long Powershell file

- replace every ; with ;\n
- first string base 64
- second variable is already decoded
- two loops
    - second one xors decoded w/ blob & replaces it in decoded
- if statement
- fetch assembly & interact
- comment out last 2 lines
- run it $\implies$many bytes

### Cyberchef

- result = dll file
- trid remnux
    - analyzes binary files

## ILSPY on dll file

- looking at Deimos class from Mars
    - shows IP

### de4dot to deobfuscate

- solarmarker.dat
- aes encryption

### Interact function

- this is a RAT trojan communicating using POSTS in json

## Anyrun

- looking up solarmarker.dat
    - confirms RAT
        - .NET
- looking at report
- part of larger Jupyter malware

