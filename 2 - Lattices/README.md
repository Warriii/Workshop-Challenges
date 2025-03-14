### Lattice Introduction (5)
Cryptohack challenges introducing the concept of lattices (and goes more in depth into LLL!)

Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
Vectors|Cryptohack|Cryptohack|-|See `LatticeIntroduction/` for links
Size and Basis|Cryptohack|Cryptohack|-|See `LatticeIntroduction/` for links
Gram Schmidt|Cryptohack|Cryptohack|-|See `LatticeIntroduction/` for links
What's a Lattice?|Cryptohack|Cryptohack|-|See `LatticeIntroduction/` for links
Gaussian Reduction|Cryptohack|Cryptohack|-|See `LatticeIntroduction/` for links

### LLL (4)
Challenges involving and demonstrating various use cases of LLL in general

Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
Find the Lattice|Cryptohack|Cryptohack|-|See `LLL/` for links
Tan|ictf 23|maple|-|-
Mobius|ictf round 27|maple|-|-
Easy DSA: LCG|ictf round 30|maple|ECDSA, LCG|-

### Knapsack / Merkle Hellman (2)
For challenges that involve the Merkle Hellman cryptosystem or similar
Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
Backpack Cryptography|Cryptohack|Cryptohack|MH|See `Knapsack_MerkleHellman/` for links
Real Eisenstein|Cryptohack|ariana|MH-ish|See `Knapsack_MerkleHellman/` for links


### LatticeEnumeration (2)
Challenges involving bruting small integer combinations of lattices, or lattice enumeration
Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
LRSA|Cyberleague Playoffs 25|warri|RSA|There's a non-lattice way to solve it, but can you do it using only LLL and manual enumeration?
onelinecrypto|seetf 23|neobeo|-|-


### HiddenNumberProblem (ECDSA) (2)
Challenges involving the Hidden Number Problem, notably the ECDSA case

Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
Same Nonce|-|warri|ECDSA|Simple introductory challenge to ECDSA. Doesn't require LLL
No Random, No Bias|Cryptohack|Cryptohack|ECDSA|See `HiddenNumberProblem_ECDSA/` for links


### LearningWithErrors (14)
Compiled list of challenges surrounding the LWE scheme, and related challenges involving them! Some may not involve LLL

Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
LearningWithErrors 1|Cryptohack|ireland|LWE|Refers to the entire category. See links in `LearningWithErrors/`
LearningWithErrors 2|Cryptohack|ireland|LWE|Refers to the entire category. See links in `LearningWithErrors/`
Just Lattice|wwf 24|yun|LWE-Regev|Doesn't require lattices, but can be sped up with LLL
Learning-With-Mistakes|grey 24|jules|RLWE|Not LLL based but is a good introduction to Ring-LWE
rolypoly|wwf 24|warri|Giophantus|-


### LCGs (4)
Challenges involving LCGs and Truncated LCGS

Chall Name | Source | Author | Cryptosystem | Details
---|---|---|---|---
beginnerLCG|blahaj 24|tomato|LCG|Regarding parameter recovery. Doesn't involve LLL
cycloLCG|blahaj 24|tomato|LCG|Doesn't involve LLL
ycloLC|blahaj 24|tomato|Truncated LCG|Involves LLL
mlfsr|ictf round 54|maple|Truncated LCG (kinda)|"just adapt the idea of stern's attack on lcg and apply a bunch of LLL"