import base64
import json
from getpass import getpass
from os import system
from os.path import exists
from pathlib import Path
from sys import platform
from time import sleep

from colorama import Fore, Back, init
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pyfiglet import Figlet

init(autoreset=True)


if platform == "linux" or platform == "linux2":
    custom_fig = Figlet(font="big")
else:
    custom_fig = Figlet(font="utopiab")


def clear():
    if platform == "linux" or platform == "linux2":
        _ = system("clear")
    else:
        _ = system("cls")


filename = input(Fore.LIGHTGREEN_EX + "JSON filename: " + Fore.RESET)


password_introduced = getpass(Fore.LIGHTRED_EX + "PASSWORD: ")
clear()
password_key = password_introduced.encode()
salt: bytes = b'\x9d\xe8j\xee\x03b\xff]\xefd\xaa]7%\x9a('
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    backend=default_backend(),
    iterations=100000)
key = base64.urlsafe_b64encode(kdf.derive(password_key))
print("\n" + Fore.LIGHTGREEN_EX + "Key generated successfully: " + Fore.LIGHTBLUE_EX)
print(Fore.BLACK + Back.RED + str(key.decode()))


def fileEncrypt():
    file_path = Path(filename)
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        original_file = file.read()
    encrypted = f.encrypt(original_file)
    print("\n" + Fore.LIGHTGREEN_EX + "File encrypted successfully!")
    sleep(1)
    clear()
    destination_path = file_path
    with open(destination_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def fileDecryption():
    file_path = Path(filename)
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        original_file = file.read()
    decrypted = f.decrypt(original_file)
    print(Fore.LIGHTGREEN_EX + "File decrypted successfully!")
    sleep(1)
    clear()
    print(Fore.CYAN + custom_fig.renderText("SHA-256"))
    print(Fore.LIGHTWHITE_EX + "Password storage | by ru55o")
    destination_path = file_path
    with open(destination_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


def addCred():
    credname = input(Fore.LIGHTYELLOW_EX + "Name (site): " + Fore.RESET)
    datos[credname] = {}

    creduser = input(Fore.YELLOW + "Username: " + Fore.RESET)
    datos[credname]["user"] = creduser

    credpass = input(Fore.YELLOW + "Password: " + Fore.RESET)
    datos[credname]["pass"] = credpass

    print(Fore.LIGHTGREEN_EX + "Credential added -> [" + Fore.LIGHTMAGENTA_EX + credname + Fore.LIGHTGREEN_EX + "]")

    json.dump(datos, open(filename, "w"), indent=4)


def displayXCred():
    credname = input(Fore.LIGHTYELLOW_EX + "Enter credential to display: " + Fore.RESET)
    result = []
    for cred in datos:
        if cred.find(credname) != -1:
            result.append(cred)
    for found_cred in result:
        print("_______________________________________")
        print("\n" + Fore.LIGHTYELLOW_EX + "[" + found_cred + "]")
        print(Fore.YELLOW + "Username: " + datos[found_cred]["user"])
        print(Fore.YELLOW + "Password: " + datos[found_cred]["pass"])
    print("_______________________________________")


def displayAllCreds():
    for cred in datos:
        print("_______________________________________")
        print("\n" + Fore.LIGHTYELLOW_EX + "[" + cred + "]")
        if datos[cred]["user"]:
            print(Fore.YELLOW + "Username: " + datos[cred]["user"])
        if datos[cred]["pass"]:
            print(Fore.YELLOW + "Password: " + datos[cred]["pass"])
    print("_______________________________________")


def removeCred():
    credname = input(Fore.LIGHTYELLOW_EX + "Credential to remove: " + Fore.RESET)
    try:
        del datos[credname]
        json.dump(datos, open(filename, "w"), indent=4)
        print(Fore.LIGHTGREEN_EX + "Credential removed successfully!")
    except KeyError:
        print(Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTMAGENTA_EX + credname + Fore.LIGHTGREEN_EX + "] doesn't exist!")
    print()


file_exists = exists(filename)
if not file_exists:
    with open(filename, "w") as f:
        f.write("{}")
        print("[" + filename + "] doesn't exist so it's been created.")
        sleep(2)
        clear()
else:
    fileDecryption()
with open(filename) as jsonfile:
    datos = json.load(jsonfile)


while True:
    print(Fore.CYAN + '''
    [0]: Save and exit
    [1]: Add a credential
    [2]: Remove a credential
    [3]: Search for a credential
    [4]: Display all credentials
    ''')
    choice = input(Fore.GREEN + "r5saver:~$ " + Fore.RESET)
    if choice == "0":
        fileEncrypt()
        quit()
    elif choice == "0!":
        clear()
        quit()
    elif choice == "1":
        addCred()
    elif choice == "2":
        removeCred()
    elif choice == "3":
        displayXCred()
    elif choice == "4":
        displayAllCreds()
    elif choice == "clear":
        clear()
    else:
        print("thats not an option!")
