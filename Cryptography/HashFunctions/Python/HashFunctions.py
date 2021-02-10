import binascii
import hashlib

text = 'Hello world!'
data = text.encode('utf-8')

sha256hash = hashlib.sha256(data).digest()
print(f'SHA-256:\t{binascii.hexlify(sha256hash).decode()}')

sha3_256 = hashlib.sha3_256(data).digest()
print(f'SHA3-256:\t{binascii.hexlify(sha3_256).decode()}')

blake2s = hashlib.new('blake2s', data).digest()
print(f'BLAKE2s:\t{binascii.hexlify(blake2s).decode()}')

ripemd160 = hashlib.new('ripemd160', data).digest()
print(f'RIPEMD-160:\t{binascii.hexlify(ripemd160).decode()}')
