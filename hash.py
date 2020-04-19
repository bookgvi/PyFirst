import hashlib
res = hashlib.sha1(b'Hello!!!')
print(res, res.hexdigest())
