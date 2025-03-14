from fastecdsa.curve import P256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
import hashlib
import random
from os import urandom
            
curve = P256
n = curve.q
k = 0
while not k:
    k = bytes_to_long(urandom(48)) % n

def generate_keys():
    priv = random.randint(1, P256.q - 1)
    pub = priv * curve.G
    return priv, pub

def sign_message(priv, m):
    H = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    R = k * curve.G
    r = R.x
    k_inv = pow(k, -1, n)
    s = (k_inv * (H + r * priv)) % n
    return r, s

def encrypt_flag(flag, priv):
    key = long_to_bytes(priv)
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(flag)
    iv = cipher.iv
    return iv, ct

flag = b'flag{??????????????????????????}'
priv, pub = generate_keys()
m0 = "Welcome to ECDSA!"
m1 = "I'm so confident this implementation is secure :)"
s0 = sign_message(priv, m0)
s1 = sign_message(priv, m1)
iv, ct = encrypt_flag(flag, priv)
print(f'{s0 = }')
print(f'{s1 = }')
print(f'{iv = }')
print(f'{ct = }')
"""
s0 = (27198383206211706429615111947647495831213920268106394186399468644845402713961, 93936951888997076856725828811640217298540985671684527351623950342582758627863)
s1 = (27198383206211706429615111947647495831213920268106394186399468644845402713961, 13109930965822393469303190696696306036889802439408423696607560702303514214812)
iv = b'\xc4K\xf8.C\x86#\xfa$E\xe7\x89\x8e\xda\x82\x8a'
ct = b'\xbeB\xc3\xc9\xd2v\x7f\x19\xe7\xe1c\x05\xea%\x1f\xcb\x03j\xdbL\xd9\x00\x1d}\xc6\xb4\x1d\x98#\x0eb\x96'
"""
