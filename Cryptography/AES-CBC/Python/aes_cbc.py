from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

iv = b'aaaaaaaaaaaaaaaa'
key = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
plaintext = 'This is a secret!'

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext.encode("utf-8"), AES.block_size))
print(f'Encryption: {ciphertext.hex()}')

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(f'Decryption: {plaintext.decode("utf-8")}')
