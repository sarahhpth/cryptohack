'''
iv ^ dec = False    what is there
x  ^ dec = True;    what we want
x is what iv should be to give us True;

dec = iv ^ False
dec = x ^ True;
iv ^ False = x ^ True;
x = iv ^ False ^ True;
'''

import requests
from pwn import xor

cookie = requests.get('http://aes.cryptohack.org/flipping_cookie/get_cookie').json()['cookie']  
cookie = bytes.fromhex(cookie)

iv = cookie[:16]
cookie = cookie[16:]

x = xor(iv, b'admin=False;expi', b'admin=True;expir')

print(requests.get('http://aes.cryptohack.org/flipping_cookie/check_admin/{}/{}/'.format(cookie.hex(), x.hex())).json())



