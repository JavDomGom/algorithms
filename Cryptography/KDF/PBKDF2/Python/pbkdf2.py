import binascii

from backports.pbkdf2 import pbkdf2_hmac

salt_str = 'aaef2d3f4d77ac66e9c5a6c3d8f921d1'
salt = binascii.unhexlify(salt_str)
passwd = 'Esta es la clave a proteger'.encode('utf8')
key = pbkdf2_hmac('sha256', passwd, salt, 50000, len(salt_str))

print(f'Derived key: {binascii.hexlify(key).decode("utf8")}')
