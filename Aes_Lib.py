from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

def print_bytes_hex(label, bytes_data):
    print(f"{label}: {bytes_data.hex()}")

# AES requires a key size of 16, 24, or 32 bytes
key = get_random_bytes(16)  # Generate a random 16-byte key for AES-128
iv = get_random_bytes(16)   # Generate a random 16-byte IV for CBC mode

print_bytes_hex("Key", key)
print_bytes_hex("IV", iv)

# Create AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Example plaintext
plaintext = b"Encrypt this message using AES!"
print("\nOriginal plaintext:", plaintext.decode())

# Encryption
padded_plaintext = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_plaintext)
print_bytes_hex("Ciphertext", ciphertext)

# Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded_plaintext = decipher.decrypt(ciphertext)
decrypted_plaintext = unpad(decrypted_padded_plaintext, AES.block_size)
print("\nDecrypted plaintext:", decrypted_plaintext.decode())