p = 1999        # Public prime number.
G = 33          # Set generator G.
secret_a = 47   # Private.
secret_b = 117  # Private.

print('1. Alice calculates "G^a mod p" to send to Bob.')
G_a_mod_p = pow(G, secret_a) % p
print(f'\t- G^a mod p: {G_a_mod_p}\n')

print('2. Bob calculates "G^b mod p" to send to Alice.')
G_b_mod_p = pow(G, secret_b) % p
print(f'\t- G^b mod p: {G_b_mod_p}\n')

print('3. Bob receives "G^a mod p" and calculates "(G^a)^b mod p".')
Gab_mod_p = pow(G_a_mod_p, secret_b) % p
print(f'\t- (G^a)^b mod p: {Gab_mod_p}\n')

print('4. Alice receives "G^b mod p" and calculates "(G^b)^a mod p".')
Gba_mod_p = pow(G_a_mod_p, secret_b) % p
print(f'\t- (G^b)^a mod p: {Gba_mod_p}\n')

print('5. Shared key between Alice and Bob is "G^(a * b) mod p".')
shared_K = pow(G, (secret_a * secret_b)) % p
print(f'\t- Shared key: {shared_K}\n')
