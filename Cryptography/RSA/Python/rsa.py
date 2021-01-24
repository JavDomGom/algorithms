# Bob vars.
p_b = 97                # Prime number, secret.
q_b = 677               # Prime number, secret.
d_b = 53771             # Private key part (d_b, n_b), secret.
e_b = 35                # Public key part (e_b, n_b), public.
n_b = p_b * q_b         # Public key part (e_b, n_b), public.

# Alice vars.
p_a = 113               # Prime number, secret.
q_a = 587               # Prime number, secret.
d_a = 18377             # Private key part (d_a, n_a), secret.
e_a = 25                # Public key part (e_a, n_a), public.
n_a = p_a * q_a         # Public key part (e_a, n_a), public.

M = 55967               # Secret msg.
print(f'0. Secret message is: {M}')

C = pow(M, e_a) % n_a   # Encrypt M as C.
print(f'1. Bob encrypts message {M} and sends it to Alice as {C}.')

print(f'2. Alice receives {C}.')

M = pow(C, d_a) % n_a   # Decrypt C as M.
print(f'3. Alice decrypts the message {C} and gets {M}.')
