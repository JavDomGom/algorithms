import pyaes
import binascii
import secrets

iv = secrets.randbits(256)
key = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
text = 'This is a secret!'

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))

ciphertext = aes.encrypt(text)
print(f'Encryption: {binascii.hexlify(ciphertext).decode("utf-8")}')

aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))

decrypted = aes.decrypt(ciphertext)
print(f'Decryption: {decrypted.decode("utf-8")}')
