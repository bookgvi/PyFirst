from Crypto.PublicKey import RSA

PATH = './keys'

key = RSA.generate(1024)
secret_key = key.exportKey(
    passphrase='QQQ',
    pkcs=8
)
with open(f'{PATH}/private_rsa_key.bin', 'wb') as f:
    f.write(secret_key)

with open(f'{PATH}/public_rsa.pem', 'wb') as f:
    f.write(key.publickey().exportKey())
