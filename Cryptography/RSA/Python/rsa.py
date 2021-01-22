# Bob vars.
n_b = 65669
e_b = 35
d_b = 53771

# Alice vars.
n_a = 66331
e_a = 25
d_a = 18377

M = 55967  # Secret msg.
print(f'0. Secret message is: {M}')

C = pow(M, e_a) % n_a  # Encrypt M as C.
print(f'1. Bob encrypts message {M} and sends it to Alice as {C}.')

print(f'2. Alice receives {C}.')

M = pow(C, d_a) % n_a  # Decrypt C as M.
print(f'3. Alice decrypts the message {C} and gets {M}.')
