from sage.all import SymmetricGroup, PermutationGroup, random_prime, save
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
from SECRET import flag

gk = random_prime(2**64, 2**65)
g = 2**4 * 5**5
G = SymmetricGroup(g)
gp, gq = G.random_element(), G.random_element()
gn = gp * gq
ge = 0x10001
GG = PermutationGroup([gp, gq])
gm = GG.random_element()
gc = (gm**gk)**ge
gi = [G.identity()(i) for i in range(g+1)]

GN = [gn(i) for i in gi[1:]]
GM = [gm(i) for i in GN]
GC = [gc(i) for i in GN]

enc = AES.new(sha256(str(gk).encode()).digest()[:16], AES.MODE_ECB).encrypt(pad(flag,16)).hex()

out = {"GN":GN, "GM":GM, "GC":GC, "enc":enc}
save(out, "out.sobj")