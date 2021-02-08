import sys

from gmpy import invert
from tinyec.ec import SubGroup, Curve

# Elliptic curve: y² = x³ + ax + b mod p

print('1. Signature keys generation and verification.') 

# Parameters:
a = 3
b = 42
p = 89
n = 79                  # Points in curve.
G = (69, 80)            # Base point generator.

field = SubGroup(p=p, g=G, n=n, h=1)
curve = Curve(a=a, b=b, field=field, name='ECDH')

print(f'\t- Curve: {curve}')

G_subgroup = [(lambda p: (p.x, p.y))(k * curve.g) for k in range(n)]

print(f'\t- G subgroup: {G_subgroup}')

rng = range(1, n)       # Range [1, n-1].

# Alice vars.
d_a = 23                # Private key. Random number in range [1, n-1].
Q_a = G_subgroup[d_a]   # Public key.
inv_K = invert(14, n)   # K⁻¹ = 14⁻¹ mod 79

if d_a in rng:
    print(f'\t- d: {d_a}')
else:
    print(f'\t- ERROR: {d_a} not in range [1, {n}].')
    sys.exit(1)

print(f'\t- Alice\'s private key: {d_a}, and public key: {Q_a}.\n')

print('2. Signature process.') 

k = 14                  # Alice selects a random number k in range [1, n-1].
print(f'\t- k: {k}')

kG = G_subgroup[k]      # kG = (x_1, y_1)
print(f'\t- kG: {kG}')

r = kG[0] % n

if r != 0:
    print(f'\t- r: {r}')
else:
    print(f'\t- ERROR: {r} = 0. If r = 0 or s = 0, choose another value k.')
    sys.exit(1)

h_m = 63                # SHA-1 hash from message to cypher.
print(f'\t- h(m): {h_m}')

s = 17 * (h_m + d_a * r) % n
print(f'\t- s: {s}')

m_sig = (r, s)
print(f'\t- m signature: {m_sig}\n')

print(f'3. Verification process.')

if r in rng and s in rng:
    print(f'\t- OK: {r} and {s} in range [1, {n}].')
else:
    print(f'\t- ERROR: {m_sig} not in range [1, {n}].')
    sys.exit(1)

w = invert(s, n)        # w = s⁻¹ mod n
print(f'\t- w: {w}')

z_1 = (h_m * w) % n     # z_1 = h(m) * w mod n
print(f'\t- z_1: {z_1}')

z_2 = (r * w) % n       # z_2 = r * w mod n
print(f'\t- z_2: {z_2}')

z_1G = G_subgroup[z_1]
print(f'\t- z_1G: {z_1G}')

field_a = SubGroup(p=p, g=Q_a, n=n, h=1)
curve_a = Curve(a=a, b=b, field=field_a, name='d_b * Q_a')
Q_a_subgroup = [(lambda p: (p.x, p.y))(k * curve_a.g) for k in range(n)]

z_2Q_a = Q_a_subgroup[z_2]
print(f'\t- z_2Q_a: {z_2Q_a}')

# EC Point addition: P(x_1, y_1) + Q(x_2, y_2) = R(x, y)
x_1 = z_1G[0]
y_1 = z_1G[1]
x_2 = z_2Q_a[0]
y_2 = z_2Q_a[1]

op_x = x_1 - x_2
op_y = y_1 - y_2

inv_op_x = invert(op_x, p)
lam = op_y * inv_op_x % p

x = (pow(lam, 2) - x_1 - x_2) % p
y = (lam * (x_1-x) - y_1) % p

print(f'\t- z_1G + z_2Q_a: ({x}, {y})')

if x == r:
    print(f'\t- OK: x ({x}) and r ({r}) are equals.')
else:
    print(f'\t- ERROR: x ({x}) and r ({r}) aren\'t equals.')
    sys.exit(1)