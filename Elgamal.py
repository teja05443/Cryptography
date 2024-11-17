import random
import configparser

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_exp(base, exp, mod):
    """Perform modular exponentiation."""
    return pow(base, exp, mod)

def generate_key(q, alpha, xa):
    """Generate public key based on q, alpha, and private key xa."""
    y_a = mod_exp(alpha, xa, q)  # y_a = alpha^xa mod q
    return y_a

def encrypt(M, q, alpha, y_a, K):
    """Encrypt the plaintext message M."""
    # Calculate the shared secret
    shared_secret = mod_exp(y_a, K, q)

    # Calculate ciphertext components
    c1 = mod_exp(alpha, K, q)  # c1 = alpha^K mod q
    c2 = (M * shared_secret) % q  # c2 = M * (y_a^K mod q)

    return c1, c2

def decrypt(c1, c2, xa, q):
    """Decrypt the ciphertext (c1, c2) using private key xa."""
    # Calculate the shared secret
    shared_secret = mod_exp(c1, xa, q)
    
    # Find the modular inverse of the shared secret
    shared_secret_inv = pow(shared_secret, -1, q)  # Modular inverse

    # Decrypt message
    M = (c2 * shared_secret_inv) % q
    return M

def string_to_int(message):
    """Convert a string message into an integer by concatenating ASCII values."""
    return int(''.join(str(ord(char)) for char in message))

def int_to_string(integer, message_type):
    """Convert an integer back into a string by breaking it into ASCII values."""
    if message_type == '2':
        # For string messages, return the encrypted message as is, as requested
        return "Encrypted message remains: " + str(integer)
    
    message = str(integer)
    # Ensure each ASCII character has a length of 3 digits (ASCII values)
    chars = [chr(int(message[i:i+3])) for i in range(0, len(message), 3)]
    return ''.join(chars)

def elgamal_encrypt_decrypt(q, alpha, xa, M, K, message_type):
    """Encrypt and then decrypt a message."""
    # Generate public key
    y_a = generate_key(q, alpha, xa)

    # Encrypt the message
    c1, c2 = encrypt(M, q, alpha, y_a, K)
    print(f"Cipher Text: (c1: {c1}, c2: {c2})")

    # Decrypt the message
    decrypted_message = decrypt(c1, c2, xa, q)
    print(f"Decrypted Message (Int): {decrypted_message}")

    # Convert back to string if message type is string
    decrypted_message_str = int_to_string(decrypted_message, message_type)
    
    return c1, c2, decrypted_message_str

# Reading message from the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Input values for q, alpha, and xa
q = int(input("Enter a prime number q: "))
alpha = int(input("Enter a primitive root alpha of q: "))
xa = int(input("Enter the private key xa: "))

# Choose message type: numeric or string
message_type = input("Enter '1' for numeric message, '2' for string message: ")

# Read the message from the config file
message = config['settings']['message']

if message_type == '1':
    # Convert message to integer for numeric message
    M = int(input("Enter the plaintext message M (as an integer): "))
else:
    # Convert the string message from the config file to an integer
    M = string_to_int(message)

# Input the random integer K
K = int(input("Enter a random integer K: "))

# Encrypt and decrypt the message
c1, c2, decrypted_message = elgamal_encrypt_decrypt(q, alpha, xa, M, K, message_type)

# Display the result
print(f"Decrypted Message (String): {decrypted_message}")
