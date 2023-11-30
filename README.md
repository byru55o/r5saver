# r5saver
## Disclaimer
KeePassXC is better. But you can use this if you prefer a more minimal interactive cli experience (also sacrificing some security and usability).
## Introduction
This is a password keeper which encrypts all your password and stores them in JSON for maximum organization. It works with the **SHA-256** algorithm by creating a key.   
## Quick guide              
As easy as it gets, make sure the passwords are decrypted with the same program (**and salt**) that it was encrypted.    
The program is very intuitive, so you won't have much trouble using it.   
To execute it on Windows:
```python r5saver.py```    
or in Linux/Mac:
```python3 r5saver.py```
## Requirements
**Python version:** 3.6 or greater is optimal, but any Python 3 should do fine.                                   
**Libraries:** base64, json, getpass, sys, os, pathlib, time, colorama, cryptography and pyfiglet.
Use the command:
```pip install -r requirements.txt```
## Features
**Save and exit**: _always_ use this option when exiting the program, if not, the json might not be encrypted and eventually it will crash.    
**Add a credential**: Self explanatory.   
**Remove a credential**: It is what it is, but it is important you specify the exact name of the credential.   
**Search for a credential**: It will print out usernames and passwords of all the credentials that begin with your search.   
**Display all credentials**: No need to explain this.
**TIP**: use "clear" to clear the screen!
## More information:
If you want the maximum security, change the salt at line 39.            
We recommend generating one yourself using os.           
Type this in python3 console:
```python
>>> import os
>>> os.urandom(16)
b"\xe0\x0fO\xc0;mf\x03\xb5<6'\xe0\xa6+6"
```
Replace salt in the script with the output of **os.urandom(16)**.           
In this case it will be:  ```salt = b"\xe0\x0fO\xc0;mf\x03\xb5<6'\xe0\xa6+6"```                      
Remember to change the salt in _any other device or copy of file_. Otherwise it will crash.   
## Problems
You can report problems [here](https://github.com/byru55o/r5saver/issues)!                      
Don't be afraid of asking questions, if it is posible, I will be answering them.
## Authors 
**ru55o**: added 32 characters key generation and SHA-256 encryption credential keeper, made search option with the help of [s0ck37](https://github.com/Kik449) Also fixed changes with Figlet fonts as previous fonts weren't supported in some GNU/Linux distributions.
## Additional info  
This script is based on my previous string and file encrypter [r5krypt](https://github.com/KRNET009/r5krypt)  
It was developed on **Pop!_OS 21.04** using **PyCharm 2021.1.3** in **Python 3.9.5 and 3.8**.
