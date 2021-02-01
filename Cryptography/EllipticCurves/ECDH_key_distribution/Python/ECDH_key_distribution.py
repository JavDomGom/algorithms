from tinyec.ec import SubGroup, Curve

# Elliptic curve: y² = x³ + ax + b mod p

# Parameters:
a = 33
b = 51
p = 71
n = 67          # Points in curve.
G = (57, 18)    # Base point generator.

field = SubGroup(p=p, g=G, n=n, h=1)
curve = Curve(a=a, b=b, field=field, name='ECDH')

print(f'curve: {curve}')

G_subgroup = [(lambda p: (p.x, p.y))(k * curve.g) for k in range(n)]

# Alice vars.
d_a = 12
Q_a = G_subgroup[d_a]

print(
    f'1. Alice generates a random secret number {d_a} and calculate Q_a = \
d_a * G = {d_a} * {G} = {Q_a}'
)

# Bob vars.
d_b = 62
Q_b = G_subgroup[d_b]

print(
    f'2. Bob generates a random secret number {d_b} and calculate Q_b = \
d_b * G = {d_b} * {G} = {Q_b}'
)

# d_b * Q_a
field_a = SubGroup(p=p, g=Q_a, n=d_a, h=1)
curve_a = Curve(a=a, b=b, field=field_a, name='d_b * Q_a')
G_a_subgroup = [(lambda p: (p.x, p.y))(k * curve_a.g) for k in range(n)]
secret_a = G_a_subgroup[d_b]

# d_a * Q_b
field_b = SubGroup(p=p, g=Q_b, n=d_b, h=1)
curve_b = Curve(a=a, b=b, field=field_b, name='d_a * Q_b')
G_b_subgroup = [(lambda p: (p.x, p.y))(k * curve_b.g) for k in range(n)]
secret_b = G_b_subgroup[d_a]

print(
    f'3. Both users exchange their public values (or keys) Q_a and Q_b, and \
calculate d_a * Q_b or d_b * Q_a, that is d_a * d_b * G = {d_a} * {d_b} * {G} \
= {d_a} * {Q_b} = {d_b} * {Q_a} = {secret_a}.'
)
print(f'\ta) {d_b} * {Q_a} = {secret_a}')
print(f'\tb) {d_a} * {Q_b} = {secret_b}')