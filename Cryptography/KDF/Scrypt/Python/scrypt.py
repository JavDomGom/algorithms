import pyscrypt

salt = b'deafbeef4d23ac44e9c5a6c3d8f9ee8c'
passwd = b'This is the key that I want to protect.'
key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)

print(f'Derived key: {key.hex()}')
