from Crypto.Util.number import *
FLAG = b"ictf{test_flag}"

while True:
  print("Let's build an RSA-2025 public key together! I provide the exponent, you provide the modulu.")
  e = getRandomNBitInteger(2025)
  N = int(input("N = "))
  assert e.bit_length() == N.bit_length() == 2025, "We failed to collaborate on a RSA-2025 key :("
  
  m = bytes_to_long(FLAG)
  c = pow(m, N, e) # I might have mixed up the exponent and modulus. oh well
  print(f"{c = }")
