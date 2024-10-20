import socket
import random

# Define the elliptic curve parameters
def is_point_on_curve(x, y, a, b, p):
    return (y ** 2) % p == (x ** 3 + a * x + b) % p

def add_points(P, Q, a, p):
    if P == (0, 0):  
        return Q
    if Q == (0, 0):  
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == y2:
        m = (3 * x1 ** 2 + a) * pow(2 * y1, -1, p) % p
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m ** 2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_multiply(k, P, a, p):
    R = (0, 0)  
    for _ in range(k):
        R = add_points(R, P, a, p)
    return R

def generate_keys(a, b, p, G, private_key):
    public_key = scalar_multiply(private_key, G, a, p)
    return public_key

def encrypt(plaintext, public_key, a, p, G, k):
    C1 = scalar_multiply(k, G, a, p)  
    C2 = add_points(scalar_multiply(k, public_key, a, p), plaintext, a, p)  
    return C1, C2

def decrypt(ciphertext, private_key, a, p):
    C1, C2 = ciphertext
    S = scalar_multiply(private_key, C1, a, p)  
    plaintext = add_points(C2, (S[0], -S[1]), a, p)  
    return plaintext

# Socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server is listening on port 8080...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Input elliptic curve parameters
a = int(input("Enter parameter a: "))
b = int(input("Enter parameter b: "))
p = int(input("Enter prime number p: "))
Gx = int(input("Enter x-coordinate of the generator point G: "))
Gy = int(input("Enter y-coordinate of the generator point G: "))
private_key = int(input("Enter the private key: "))

# Define generator point G
G = (Gx, Gy)

if not is_point_on_curve(Gx, Gy, a, b, p):
    print("Generator point is not on the curve!")
    conn.close()
    exit()

# Generate public key
public_key = generate_keys(a, b, p, G, private_key)
print(f"Private Key: {private_key}, Public Key: {public_key}")

# Receive plaintext message from client (as a pair of integers)
plaintext_str = conn.recv(1024).decode()
plaintext = tuple(map(int, plaintext_str.split(',')))
if not is_point_on_curve(plaintext[0], plaintext[1], a, b, p):
    print("Received plaintext is not on the curve!")
    conn.close()
    exit()
print(f"Received Plaintext: {plaintext}")

# Receive random integer K from the client
k = int(conn.recv(1024).decode())
print(f"Received Random Integer K: {k}")

# Encrypt the plaintext
ciphertext = encrypt(plaintext, public_key, a, p, G, k)
print(f"Cipher Text: {ciphertext}")

# Send ciphertext back to client
conn.sendall(f"{ciphertext[0]},{ciphertext[1]}".encode())

# Receive 
