from gmpy import invert
from tinyec.ec import SubGroup, Curve

# Elliptic curve: y² = x³ + ax + b mod p

# Parameters:
a = 3
b = 42
p = 89
n = 79                  # Points in curve.
G = (69, 80)            # Base point generator.

field = SubGroup(p=p, g=G, n=n, h=1)
curve = Curve(a=a, b=b, field=field, name='ECDH')

print(f'curve: {curve}')

G_subgroup = [(lambda p: (p.x, p.y))(k * curve.g) for k in range(n)]

# Alice vars.
d_a = 23                # Private key.
Q_a = G_subgroup[d_a]   # Public key.
inv_K = invert(14, 79)  # K⁻¹ = 14⁻¹ mod 79

h_m = 63            # SHA-1 hash from message to cypher.
k = 14
kG = G_subgroup[k]
r = 67
