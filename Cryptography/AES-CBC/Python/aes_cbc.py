from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

iv = b'aaaaaaaaaaaaaaaa'
key = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
text = 'This is a secret!'

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(text.encode("utf-8"), AES.block_size))
print(f'Encryption: {ciphertext.hex()}')

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(f'Decryption: {pt.decode("utf-8")}')
