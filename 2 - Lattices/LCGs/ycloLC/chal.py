from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secrets import randbelow

FLAG = "blahaj{iS_1t_5t1LL_4_reGul4r_LCG_Aft3r_aLl?}"

def ycloLC(a, m, x, cs):
    while True:
        x = (a * x + cs[0]) % m
        yield x
        cs = cs[1:] + cs[:1]

m = getPrime(128)
a, x, *cs = [randbelow(m) for _ in range(5)] # 3 increments
rng = ycloLC(a, m, x, cs)

while True:
    option = input("""[1] See output
[2] Encrypt flag
[3] Decrypt message
""")
    if option == "1":
        output = next(rng)
        print("?"*10+str(output)[10:-10]+"?"*10)
    elif option == "2":
        output = next(rng)
        key = AES.new(pad(long_to_bytes(output), 16), AES.MODE_CBC)
        enc = key.encrypt(pad(FLAG.encode(), 16))
        print(enc.hex())
        print(key.iv.hex())
    elif option == "3":
        output = next(rng)
        ct = bytes.fromhex(input("Enter ciphertext hex: "))
        iv = bytes.fromhex(input("Enter iv hex: "))
        key = AES.new(pad(long_to_bytes(output), 16), AES.MODE_CBC, iv=iv)
        dec = key.decrypt(pad(ct, 16))
        print(dec)
    else:
        quit()