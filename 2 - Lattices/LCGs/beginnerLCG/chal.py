from Crypto.Util.number import getPrime, bytes_to_long
from secrets import randbelow

FLAG = "blahaj{thr33_eqns_thr33_var1ables_supER_cr4zy!}"
f = bytes_to_long(FLAG.encode())

def LCG(a, m, x, c):
    while True:
        x = (a * x + c) % m
        yield x

m = getPrime(128)
# you can have m
print(f"{m = }")
# but i'll derive all the other parameters from the secret flag!
a = f % m
x = (f >> 128) % m
c = (f >> 256) % m
rng = LCG(a, m, x, c)

outputs_left = 3

while True:
    option = input(f"""[1] See output ({str(outputs_left)} outputs left)
[2] Check flag
""")
    if option == "1":
        if outputs_left > 0:
            output = next(rng)
            print(output)
            outputs_left-=1
        else:
            print("You know too much!")
    elif option == "2":
        print("Prove you know the flag!")
        print("Whats a?")
        if str(a) != input():
            continue
        print("Whats c?")
        if str(c) != input():
            continue
        print("Ok, you must know the flag then... here it is:")
        print(FLAG)
        quit()
    else:
        quit()