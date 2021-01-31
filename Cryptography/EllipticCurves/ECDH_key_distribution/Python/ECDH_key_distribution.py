# Elliptic curve: y² = x³ + ax + b mod p

# Parameters:
a = 33
b = 51
p = 71
n = 67 # Points in curve.
G = (57, 18) # Base point generator.

# Alice vars.
d_a = 12

print(f'1. Alice generates a random secret number {d_a} and calculate Q_a = d_a * G = {d_a} * {str(G)}')