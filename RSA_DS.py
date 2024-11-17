from hashlib import sha256

# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse of e modulo phi
def modular_inverse(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1, temp2 = divmod(temp_phi, e)
        temp_phi, e = e, temp2
        x, y = x2 - temp1 * x1, d - temp1 * y1
        x2, x1, d, y1 = x1, x, y1, y
    if temp_phi == 1:
        return d + phi

# RSA signing and verification
def rsa_sign_and_verify():
    # Given values
    p = 11
    q = 23
    e = 3
    M = 111  # Message to sign

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Ensure e and phi are coprime
    if gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime. Choose a different e.")

    # Calculate private key d
    d = modular_inverse(e, phi)

    # Display public and private keys
    public_key = (e, n)
    private_key = (d, n)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}\n")

    # Signing the message
    print("Signing the message...")
    signature = pow(M, d, n)  # Signature: M^d mod n
    print(f"  Message: {M}")
    print(f"  Signature: {signature}\n")

    # Verifying the signature
    print("Verifying the signature...")
    verified_message = pow(signature, e, n)  # Verified message: Signature^e mod n
    print(f"  Signature Verified Message: {verified_message}")
    print(f"  Verification Match: {M == verified_message}")

    # Check if the signing and verification match
    if M == verified_message:
        print("\nSignature and Verification Match! The process is successful.")
    else:
        print("\nSignature and Verification Failed! The process is unsuccessful.")

# Run the RSA signing and verification
rsa_sign_and_verify()
