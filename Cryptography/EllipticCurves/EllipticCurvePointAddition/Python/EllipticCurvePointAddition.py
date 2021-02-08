from gmpy import invert

# Elliptic curve: y² = x³ + ax + b mod p

# Parameters:
a = 1
b = 1
p = 17

# Example: R(x, y) = P+Q = P(x_1, y_1)+Q(x_2, y_2) = P(9, 5)+Q(4, 1) = R(6, 11)
x_1 = 9
y_1 = 5
x_2 = 4
y_2 = 1

print('1. y_1 - y_2 ; x_1 - x_2')

op_x = x_1 - x_2
op_y = y_1 - y_2

inv_op_x = invert(op_x, p)

print(
    f'2. 1/(x_1 - x_2) mod p = \
1/{op_x} mod {p} = {op_x}⁻¹ mod {p} = {inv_op_x}'
)

lam = op_y * inv_op_x % p

print(
    f'3. λ = (y_1 - y_2)/(x_1 - x_2) mod p = \
{op_y}/{op_x} mod {p} = \
({op_y} mod {p})*({op_x}⁻¹ mod {p}) = \
{op_y}*{inv_op_x} mod {p} = {lam}'
)

x = (pow(lam, 2) - x_1 - x_2) % p

print(
    f'4. x = λ² - x_1 - x_2 mod p = \
{lam}²-{x_1}-{x_2} mod {p} = {pow(lam, 2)-x_1-x_2} mod {p} = {x}'
)

y = (lam * (x_1-x) - y_1) % p

print(
    f'5. y = λ(x_1 - x) - y_1 mod p = \
{lam}({x_1}-{x})-{y_1} mod {p} = \
{lam*(x_1-x)-y_1} mod {p} = {y}'
)
