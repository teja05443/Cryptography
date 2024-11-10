from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

# DES requires 8-byte key
key = get_random_bytes(8)  # generate a random 8-byte key
cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode here for simplicity

# Example plaintext
plaintext = b"DESencrypt"  # The plaintext should be a multiple of 8 bytes

# Encryption
padded_plaintext = pad(plaintext, DES.block_size)  # Pad plaintext to match block size
ciphertext = cipher.encrypt(padded_plaintext)
print("Ciphertext:", ciphertext)

# Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded_plaintext = decipher.decrypt(ciphertext)
decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size)  # Unpad decrypted text
print("Decrypted Plaintext:", decrypted_plaintext)
