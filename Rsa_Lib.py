from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Random import get_random_bytes

def rsa_example():
    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    # Create cipher object for encryption
    cipher = PKCS1_OAEP.new(public_key)
    
    # Original message
    message = b"This is a secret message for RSA encryption"
    print("Original message:", message.decode())

    # Encrypt the message
    ciphertext = cipher.encrypt(message)
    print("Encrypted:", ciphertext.hex())

    # Create cipher object for decryption
    decipher = PKCS1_OAEP.new(private_key)
    
    # Decrypt the message
    decrypted_message = decipher.decrypt(ciphertext)
    print("Decrypted message:", decrypted_message.decode())

print("=== RSA Encryption/Decryption ===")
rsa_example()