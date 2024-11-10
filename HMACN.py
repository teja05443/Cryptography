import hashlib

def sha512(data: bytes) -> bytes:
    """Helper function to return the SHA-512 hash of the input data."""
    return hashlib.sha512(data).digest()

def hmac_sha512(key: bytes, message: bytes) -> str:
    # SHA-512 block size is 128 bytes
    block_size = 128

    # Ensure the key is the correct length
    if len(key) > block_size:
        # If the key is longer than block size, hash it to reduce its size
        key = sha512(key)
    elif len(key) < block_size:
        # If the key is shorter, pad it with zeros
        key = key.ljust(block_size, b'\x00')

    # Create the inner and outer padding
    ipad = bytes((x ^ 0x36) for x in key)
    opad = bytes((x ^ 0x5C) for x in key)

    # Perform inner hash
    inner_hash = sha512(ipad + message)

    # Perform outer hash
    outer_hash = sha512(opad + inner_hash)

    # Return the final HMAC result as a hexadecimal string
    return outer_hash.hex()

# Example usage
key = b'secret_key'
message = b'This is a message to authenticate.'
hmac_result = hmac_sha512(key, message)

print("HMAC-SHA-512:", hmac_result)
