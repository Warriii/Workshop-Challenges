from fastecdsa.curve import P256
import hashlib
import random
            
curve = P256
n = curve.q

def mod_inv(a, p):
    return pow(a, p-2, p) # fermat's little theorem and modular division!


def generate_keys():
    priv = random.randint(1, P256.q - 1)
    pub = priv * curve.G
    return priv, pub


def sign_message(priv, m):
    H = int(hashlib.sha256(m.encode()).hexdigest(), 16)

    while True:
        k = random.randint(1, n - 1)
        R = k * curve.G
        r = R.x % n
        if r == 0:
            continue
        break

    k_inv = mod_inv(k, n)
    s = (k_inv * (H + r * priv)) % n
    return r, s


def verify_signature(pub, m, sig):
    r, s = sig
    if r == 0 or s == 0:
        print("Hey what are you trying to do >:(")
        return False
    
    H = int(hashlib.sha256(m.encode()).hexdigest(), 16)
    w = mod_inv(s, n)

    u1 = (H * w) % n
    u2 = (r * w) % n

    P = u1 * curve.G + u2 * pub
    return (P.x % n) == (r % n) # hmm...


if __name__ == "__main__":
    priv, pub = generate_keys()
    msg = "Welcome to ECDSA!"
    sig = sign_message(priv, msg)

    print("=============")
    print("Public Key:")
    print(pub)
    print("=============")
    print("Message:", msg)
    print("Signature r:", sig[0])
    print("Signature s:", sig[1])
    print("Verification:", verify_signature(pub, msg, sig))
    print("=============")

    print("With ECDSA this must now be secure!")
    code = str(input("Enter m: "))
    r = int(input("Enter sig r: "))
    s = int(input("Enter sig s: "))
    if verify_signature(pub, code, (r,s)):
        print("Verified!")
        eval(code)
    else:
        print("Verification Failed!")
