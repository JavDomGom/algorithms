from argon2 import hash_password_raw, low_level
import binascii

hash = hash_password_raw(
    time_cost=16,
    memory_cost=2**15,
    parallelism=2,
    hash_len=32,
    password=b'My secret password',
    salt=b'0123456789ABCDEF',
    type=low_level.Type.ID
)

print(f'Argon2id hash: {binascii.hexlify(hash).decode("utf-8")}')
