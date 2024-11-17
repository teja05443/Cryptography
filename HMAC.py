import hashlib

def sha512(data):
    return hashlib.sha512(data).digest()

def hmac_sha512(key,message):

    block_size=128

    if len(key) > block_size:
        key = sha512(key) # Hash the key
    if len(key) < block_size:
        key = key.ljust(block_size, b'\x00') # Pad the zero's ti make it equal to the block size
    
    ipad = bytes((x ^ 0x36)for x in key)
    opad = bytes((x ^ 0x5c)for x in key)

    inner_hash = sha512(ipad + message)
    hmac_result = sha512(opad + inner_hash)

    return hmac_result

key = b"my_secret_key"
message = b"This is the message to authenticate."
hmac_result = hmac_sha512(key,message)
print("The hash value is ",hmac_result.hex())
