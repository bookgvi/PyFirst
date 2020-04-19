from Crypto.Cipher import DES

key = 'abcdefgh'
stringToEncrypt = 'QQQ'


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)
paddedText = pad(stringToEncrypt)
res = des.encrypt(paddedText)
print(res)
print(des.decrypt(res))
