import random
from hashlib import sha256

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

# Function to compute gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# DSS Implementation
def dss_digital_signature():
    # Prime number p, q, and generator g
    p = 23  # Example prime (use larger primes for real applications)
    q = 11  # Prime divisor of p-1
    g = 2   # g^q mod p = 1

    # Private key x (randomly selected)
    x = random.randint(1, q - 1)

    # Public key y = g^x mod p
    y = pow(g, x, p)

    print(f"Public Key: (p={p}, q={q}, g={g}, y={y})")
    print(f"Private Key: x={x}\n")

    # Input message (numeric or string)
    message = input("Enter the message to sign: ")

    # Convert the message into a hash value
    if message.isdigit():
        hashed_message = int(message) % q  # Numeric message
    else:
        hashed_message = int(sha256(message.encode()).hexdigest(), 16) % q  # String message

    print(f"\nHash of the Message: {hashed_message}")

    # Signing the message
    print("\nSigning the message...")
    while True:
        k = random.randint(1, q - 1)
        if gcd(k, q) == 1:  # k must be coprime to q
            break
    r = pow(g, k, p) % q
    k_inverse = modular_inverse(k, q)
    s = (k_inverse * (hashed_message + x * r)) % q

    print(f"  Signature: (r={r}, s={s})\n")

    # Verifying the signature
    print("Verifying the signature...")
    if r <= 0 or r >= q or s <= 0 or s >= q:
        print("\nSignature Invalid! (r, s out of bounds)")
        return

    w = modular_inverse(s, q)
    u1 = (hashed_message * w) % q
    u2 = (r * w) % q
    v = (pow(g, u1, p) * pow(y, u2, p) % p) % q

    print(f"  Computed v: {v}")
    print(f"  Signature r: {r}")
    print(f"  Verification Match: {v == r}")

    # Check if the signing and verification match
    if v == r:
        print("\nSignature and Verification Match! The process is successful.")
    else:
        print("\nSignature and Verification Failed! The process is unsuccessful.")

# Run the DSS implementation
dss_digital_signature()
