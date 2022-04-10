import requests
from pwn import xor

url = 'http://aes.cryptohack.org/ecbcbcwtf/'

def decrypt(ciphertext):
    return requests.get(url + 'decrypt/' + ciphertext).json()['plaintext']

def split(text, size):
    return [text[i:i+size] for i in range(0, len(text), size)]

ct = requests.get(url + 'encrypt_flag').json()['ciphertext']
ct = split(ct, 32)

for i in range(1, len(ct)):
    print(xor(bytes.fromhex(ct[i-1]), bytes.fromhex(decrypt(ct[i]))))
