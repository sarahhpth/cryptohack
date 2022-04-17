import requests
from pwn import xor

PNG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'

ciphertext = bytes.fromhex(requests.get('http://aes.cryptohack.org/bean_counter/encrypt').json()['encrypted'])
key = xor(ciphertext[:16], PNG)

plaintext = xor(ciphertext, key)
with open('beanflag.png', 'wb') as f:
    f.write(plaintext)