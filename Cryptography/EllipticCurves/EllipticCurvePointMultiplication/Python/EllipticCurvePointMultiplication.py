from gmpy import invert

# Elliptic curve: y² = x³ + ax + b mod p

# Parameters:
a = 1
b = 1
p = 17

# Example: R(x, y) = 2 * P = 2 * P(x_1, y_1) = 2 * P(6, 6) = R(9, 5)
x_1 = 6
y_1 = 6

op_x_1 = 3*pow(x_1, 2)+1
inv_2y_1 = invert(2*y_1, p)
lam = op_x_1*inv_2y_1 % p

print(
    f'1. λ = (3 * x_1² + 1)/2 * y_1 mod p = \
(3 * {x_1}² + 1)/2 * {y_1} mod {p} = \
{op_x_1}/{2*y_1} mod {p} = \
{op_x_1} mod {p} * {2*y_1}⁻¹ mod {p} = \
{op_x_1} * {inv_2y_1} mod {p} = {lam}'
)

x = (pow(lam, 2) - 2 * x_1) % p

print(
    f'2. x = λ² - 2 * x_1 mod p = \
{pow(lam, 2)} - 2 * {x_1} mod {p} = {x}'
)

op_lam = lam * (x_1 - x)
y = (op_lam - y_1) % p

print(
    f'3. y = λ(x_1 - x) - y_1 mod p = \
{lam}({x_1} - {x}) - {y_1} mod {p} = \
{op_lam} - {y_1} mod {p} = \
{op_lam - y_1} mod {p} = {y}'
)
