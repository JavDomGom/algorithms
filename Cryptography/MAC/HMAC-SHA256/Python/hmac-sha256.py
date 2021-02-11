import hashlib
import hmac
import binascii


def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()


key = b'James Bond 007'
msg = b'This is a secret message!'

print(binascii.hexlify(hmac_sha256(key, msg)).decode('utf-8'))
