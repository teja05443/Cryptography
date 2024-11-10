from Cryptodome.Util.number import getPrime
from Cryptodome.Random import get_random_bytes
import random

def generate_keys(key_size):
    # Generate prime p
    p = getPrime(key_size)
    # Find generator g
    g = 2
    # Generate private key
    x = random.randint(2, p-2)
    # Calculate public key
    h = pow(g, x, p)
    return (p, g, h), x

def encrypt(public_key, message, k=None):
    p, g, h = public_key
    if k is None:
        k = random.randint(2, p-2)
    # Calculate shared secret
    s = pow(h, k, p)
    # Calculate c1 and c2
    c1 = pow(g, k, p)
    c2 = (message * s) % p
    return (c1, c2)

def decrypt(private_key, p, cipher_text):
    c1, c2 = cipher_text
    # Calculate shared secret
    s = pow(c1, private_key, p)
    # Calculate modular multiplicative inverse
    s_inv = pow(s, p-2, p)
    # Decrypt message
    return (c2 * s_inv) % p

def elgamal_example():
    # Generate keys
    public_key, private_key = generate_keys(64)
    p, g, h = public_key
    
    # Original message (convert to integer for simplicity)
    message = 12345
    print("Original message:", message)

    # Encrypt
    cipher_text = encrypt(public_key, message)
    print("Encrypted:", cipher_text)

    # Decrypt
    decrypted_message = decrypt(private_key, p, cipher_text)
    print("Decrypted message:", decrypted_message)

print("\n=== ElGamal Encryption/Decryption ===")
elgamal_example()