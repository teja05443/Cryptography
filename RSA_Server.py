import socket
import random

# Prime number generation
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# GCD and Modular Inverse Functions
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = gcd_extended(b, a % b)
    return d, y, x - (a // b) * y

def mod_inverse(a, n):
    d, x, _ = gcd_extended(a, n)
    if d == 1:
        return x % n
    else:
        return None

# Encryption and Decryption
def Encrypt(m, e, n):
    return pow(m, e, n)

def Decrypt(c, d, n):
    return pow(c, d, n)

# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server is listening on port 8080...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# User input for p and q
p = int(input("Enter a prime number p: "))
q = int(input("Enter a prime number q: "))

# Verify that p and q are prime
if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime.")
    conn.close()
    exit()

n = p * q
phi_n = (p - 1) * (q - 1)

# Choose e explicitly, e should be relatively prime to phi_n
e = 3  # As an example; you can add checks to ensure it meets the criteria

# Check if e is valid
if gcd(e, phi_n) != 1:
    print("Chosen e is not valid, it must be coprime with phi(n).")
    conn.close()
    exit()

# Calculate d
d = mod_inverse(e, phi_n)

print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d, n): ({d}, {n})")

# Send public key to client
conn.sendall(f"{e},{n}".encode())

# Receive the encoded message (cipher text) from the client
cipher_text = int(conn.recv(1024).decode())
print(f"Received Cipher Text: {cipher_text}")

# Decrypt the message
decrypted_message = Decrypt(cipher_text, d, n)
print(f"Decrypted Text (as number): {decrypted_message}")

# Convert decrypted number back to string
decoded_string = ''
while decrypted_message > 0:
    decoded_string = chr((decrypted_message % 100) + ord('A')) + decoded_string
    decrypted_message //= 100

print(f"Decoded String: {decoded_string}")

# Close the connection
conn.close()
    