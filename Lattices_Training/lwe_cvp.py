from sage.all import Matrix, vector, VectorSpace, GF, randint, ZZ
from hashlib import sha256

n = 5
p = 3
q = 257
              
flag = b"flag{???????????????????????????????????????????????}"
F = GF(q) # our field (you can just treat this as positive integers modulo q)
V = VectorSpace(F, n) # Zqn
S = V.random_element()

def encrypt(S, k): # get k different a*s/q + e values 
    A = Matrix([V.random_element() for i in range(k)])
    e = vector([randint(-p, p) for i in range(k)])
    b = A * S + e
    return A, b

def encrypt_flag(msg, S): # call encrypt_flag(ciphertext, S) when you recover S to get the msg back!
    xor_key = sha256(str(list(S)).encode()).digest()
    ciphertext = [msg[i] ^ xor_key[i % len(xor_key)] for i in range(len(msg))]
    return bytes(ciphertext)

k = 10
A, b = encrypt(S, k)
print(f'{A = }')
print(f'{b = }')

ciphertext = encrypt_flag(flag, S)
print(f'{ciphertext = }')
"""
A = [  1 167  69  39 113]
[225 177 108 194 252]
[ 56 177  25  54  46]
[253 245 112 243  10]
[160   5 125 125 119]
[209 138  29 131  51]
[182 198  80 166 180]
[198 102 237 193  56]
[115 111 173  53 158]
[128 142   8 158 146]
b = (90, 107, 235, 87, 209, 158, 158, 235, 67, 112)
ciphertext = b'\x0f\xc2\xfbP^w\x06\xf1\xd7\x84*\xa8,,\x1b\x15U\x98\xb0Z\xf27 \xa3l\xa4\xad\xf1\xce\xb8\x05&\x06\xcb\xe9YQ[\x18\xe4\xd4\x98*\xa1?*\x00\x0ei\x8d\xa2\t\xee'
"""