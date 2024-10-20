import socket
import random

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
    # Compute public key y_a = alpha^xa mod q
    y_a = mod_exp(alpha, xa, q)
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

# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server is listening on port 8080...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive input values q, alpha, xa
input_data = conn.recv(1024).decode()
q, alpha, xa = map(int, input_data.split(','))
print(f"Received values -> q: {q}, alpha: {alpha}, xa: {xa}")

# Generate public key
y_a = generate_key(q, alpha, xa)
print(f"Public Key (y_a): {y_a}")

# Receive message M and random integer K
data = conn.recv(1024).decode()
M, K = map(int, data.split(','))
print(f"Received Message (M): {M}, Random Integer (K): {K}")

# Encrypt the message
c1, c2 = encrypt(M, q, alpha, y_a, K)
print(f"Cipher Text: (c1: {c1}, c2: {c2})")

# Send the ciphertext back to the client
conn.sendall(f"{c1},{c2}".encode())

# Receive ciphertext for decryption
cipher_text = conn.recv(1024).decode()
c1, c2 = map(int, cipher_text.split(','))
# Decrypt the message
decrypted_message = decrypt(c1, c2, xa, q)
print(f"Decrypted Message: {decrypted_message}")

# Close the connection
conn.close()
