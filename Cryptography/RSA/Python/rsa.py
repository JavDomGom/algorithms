# Bob vars.
p_b = 97         # Prime number, secret.
q_b = 677        # Prime number, secret.
e_b = 35         # Part of the pub/priv keys.
d_b = 53771      # Public key part (d_b, e_b), secret.
n_b = p_b * q_b  # Private key part (n_b, e_b).

# Alice vars.
p_a = 113        # Prime number, secret.
q_a = 587        # Prime number, secret.
e_a = 25         # Part of the pub/priv keys.
d_a = 18377      # Public key part (d_b, e_b), secret.
n_a = p_a * q_a  # Private key part (n_a, e_a).

M = 55967  # Secret msg.
print(f'0. Secret message is: {M}')

C = pow(M, e_a) % n_a  # Encrypt M as C.
print(f'1. Bob encrypts message {M} and sends it to Alice as {C}.')

print(f'2. Alice receives {C}.')

M = pow(C, d_a) % n_a  # Decrypt C as M.
print(f'3. Alice decrypts the message {C} and gets {M}.')
