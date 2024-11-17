import random
from hashlib import sha256

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute modular inverse
def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q, a, m = a // m, m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# ElGamal Digital Signature Scheme
def elgamal_digital_signature():
    # Prime number p and generator g
    p = 23  # Example prime (use larger primes for real applications)
    g = 7   # Primitive root modulo p

    # Private key x 
    x = int(input("Enter the private key of the user: " ))

    # Public key y = g^x mod p
    y = pow(g, x, p)

    print(f"Public Key: (p={p}, g={g}, y={y})")
    print(f"Private Key: x={x}\n")

    # Input message (as a string)
    message = input("Enter the message to sign: ")

    # Convert the message into a hash value
    hashed_message = int(sha256(message.encode()).hexdigest(), 16) % p

    print(f"\nHash of the Message: {hashed_message}")

    # Signing the message
    print("\nSigning the message...")
    while True:
        k = int(input("Enter the random K value : "))
        if gcd(k, p - 1) == 1:  # k must be coprime to p-1
            break
    r = pow(g, k, p)
    k_inverse = modular_inverse(k, p - 1)
    s = (k_inverse * (hashed_message - x * r)) % (p - 1)

    print(f"  Signature: (r={r}, s={s})\n")

    # Verifying the signature
    print("Verifying the signature...")
    v1 = pow(y, r, p) * pow(r, s, p) % p
    v2 = pow(g, hashed_message, p)
    print(f"  Computed v1: {v1}")
    print(f"  Computed v2: {v2}")
    print(f"  Verification Match: {v1 == v2}")

    # Check if the signing and verification match
    if v1 == v2:
        print("\nSignature and Verification Match! The process is successful.")
    else:
        print("\nSignature and Verification Failed! The process is unsuccessful.")

# Run the ElGamal Digital Signature Scheme
elgamal_digital_signature()
