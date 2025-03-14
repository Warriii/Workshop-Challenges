from Crypto.Util.number import getPrime
import random

SZ = 64
class LCG():
    def __init__(self):
        self.M = getPrime(SZ)
        self.a = random.getrandbits(SZ) % self.M # might try getPrime to see if its more lattice friendly
        self.c = random.getrandbits(SZ) % self.M
        self.x = random.getrandbits(SZ) % self.M

    def next(self):
        res = self.x >> (SZ // 2)
        rr = self.x
        self.x = (self.a * self.x + self.c) % self.M
        return res, rr
    
lcg = LCG()
a, c, m = lcg.a, lcg.c, lcg.M
y0, x0 = lcg.next()
y1, x1 = lcg.next()
y2, x2 = lcg.next()
y3, x3 = lcg.next()
y0, y1, y2, y3 = y0 << (SZ // 2), y1 << (SZ // 2), y2 << (SZ // 2), y3 << (SZ // 2)

z0, z1, z2, z3 = x0 - y0, x1 - y1, x2 - y2, x3 - y3
zs = [z0, z1, z2, z3]
xs = [x0, x1, x2, x3]
ys = [y0, y1, y2, y3]
print(f'{ys = }')