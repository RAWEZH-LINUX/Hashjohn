
import hashlib
from colorama import init
from time import *
from termcolor import colored
import sys
import os
import hashlib, binascii
from colorama import Fore, Back, Style
hash = ""

init()

print( Fore.RED+'''
●🔥════════════════════════◄►═══════════════════🔥●  
██╗░░░██╗██████╗░███╗░░██╗░█████╗░███╗░░░███╗  
██║░░░██║╚════██╗████╗░██║██╔══██╗████╗░████║  
╚██╗░██╔╝░█████╔╝██╔██╗██║██║░░██║██╔████╔██║  
░╚████╔╝░░╚═══██╗██║╚████║██║░░██║██║╚██╔╝██║ 
░░╚██╔╝░░██████╔╝██║░╚███║╚█████╔╝██║░╚═╝░██║ 
░░░╚═╝░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝  
 Telegram:https://t.me/V3n0M_Cyber                                    
 YouTube:V3n0m Cyber ✪         vercon 1.0   
●🔥════════════════════════◄►═══════════════════🔥●                     
''')

os.system("xdg-open https://t.me/V3n0M_Cyber")
hash =input("Creating Hash: ")
result = hashlib.md5(hash.encode())
print(Fore.RED +"[+]Hash MD5: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
sleep(1.0)
result = hashlib.sha1(hash.encode())
print(Fore.RED +"[+]Hash SHA1: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
sleep(1.0)
result = hashlib.sha224(hash.encode())
print(Fore.RED +"[+]Hash SHA224: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
sleep(1.0)
result = hashlib.sha256(hash.encode())
print(Fore.RED+"[+]Hash SHA256: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
sleep(1.0)
result = hashlib.sha384(hash.encode())
print(Fore.RED+"[+]Hash SHA384: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
sleep(1.1)
result = hashlib.sha512(hash.encode())
print(Fore.RED+"[+]Hash SHA512: ",end="")
print(result.hexdigest())
print("●════════════════════════════●")
print("Hash Crack website ")
print("Bo Ragrtn CTRL+Z Dabgra ")
sleep(3)
sleep(200)
v= os.system("clear")
