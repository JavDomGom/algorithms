from gmpy import invert

# Bob vars.
p_b = 2017                       # Public number.
a_b = 5                          # Public number.
K_priB = 491                     # Bob's private key.
K_pubB = pow(a_b, K_priB) % p_b  # Bob's public key.

N = 1234                         # Secret number.

# Alice vars.
v = 1810                         # Random session number.
N_1 = pow(a_b, v) % p_b          # Part of pair (N_1, N_2).
N_2 = N * pow(K_pubB, v) % p_b   # Part of pair (N_1, N_2).

# Alice send to Bob the pair (N_1, N_2), and Bob calculate:
N_3 = pow(N_1, K_priB) % p_b
N_decrypted = N_2 * invert(N_3, p_b) % p_b

print(f'Secret number is: {N_decrypted}')
