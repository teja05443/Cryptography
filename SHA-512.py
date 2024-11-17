import hashlib

def sha512_val(data):
    sha512 = hashlib.sha512()
    sha512.update(data.encode('utf-8'))
    return sha512.hexdigest()

data = "Hello World"
hash_val = sha512_val(data)
print("The hash value is :",hash_val)