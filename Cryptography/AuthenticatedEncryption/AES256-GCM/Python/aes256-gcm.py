import binascii
import json
import os

from Crypto.Cipher import AES


def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(encryptedMsg, secretKey):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


secretKey = os.urandom(32)  # 256-bit random encryption key.

print(f'Encryption key: {binascii.hexlify(secretKey).decode("utf-8")}')

msg = b'Este es el mensaje de ejemplo para un AES-256-GCM'
encryptedMsg = encrypt_AES_GCM(msg, secretKey)
data = {
    'ciphertext': binascii.hexlify(encryptedMsg[0]).decode('utf-8'),
    'aesIV': binascii.hexlify(encryptedMsg[1]).decode('utf-8'),
    'authTag': binascii.hexlify(encryptedMsg[2]).decode('utf-8')
}

print(f'Encrypted message data : {json.dumps(data, indent=4)}')

decryptedMsg = decrypt_AES_GCM(encryptedMsg, secretKey)

print(f'Decrypted message: {decryptedMsg.decode("utf-8")}')
