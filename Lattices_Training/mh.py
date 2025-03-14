from random import randint
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

BLOCK_LENGTH = 24

def keygen():
    Ws = [2]
    for _ in range(BLOCK_LENGTH):
        Ws.append(sum(Ws) + randint(1, 1337))
    q = getPrime(2 * BLOCK_LENGTH) # should be sufficient for it to be higher than sum(Ws)
    assert q > sum(Ws)
    r = randint(2, q-1)
    B = [w*r % q for w in Ws]
    return B, (Ws, q, r)

def encrypt(pub, msg):
    ciphertext = []
    block_sz = BLOCK_LENGTH // 8
    for i in range(0, len(msg), block_sz):
        msgstr = format(bytes_to_long(msg[i:i+block_sz]), f"0{BLOCK_LENGTH}b")
        enc_out = 0
        for ptr, bit in enumerate(msgstr):
            if bit == "1":
                enc_out += pub[ptr]
        ciphertext.append(enc_out)
    return ciphertext


pub, priv = keygen()
msg = b"flag{??????????????????????????????}"
cts = encrypt(pub, msg)

print(f'{pub = }')
print(f'{cts = }')
"""
pub = [40024303692548, 64831206987688, 18679118164978, 206804384094095, 112686032959809, 68662628223373, 72901248573005, 73362589959618, 81320144607439, 157512279345688, 148799558791022, 38440918841454, 175942821653306, 203284793439557, 60327908878833, 212700677676385, 84861515545788, 174684411750604, 68865439233048, 66864574864785, 88743465377994, 18130173520067, 45276021613757, 129909830079414, 111218810291773]
cts = [1284073336241683, 1577761234636958, 1284579951986903, 1297181570959999, 1677650095834617, 1454962431650670, 1573613820212016, 1343532364083779, 1321578285275325, 1557995925796838, 1715037356049921, 1437467066246051]
"""