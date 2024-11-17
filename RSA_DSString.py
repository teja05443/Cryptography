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

# RSA signing and verification for strings
def rsa_sign_and_verify():
    # Given values
    p = 11
    q = 23
    e = 3

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

    # Input message (as a string)
    message = input("Enter the message to sign: ")

    # Convert the message to a hash value
    hashed_message = int(sha256(message.encode()).hexdigest(), 16) % n

    # Signing the message
    print("\nSigning the message...")
    signature = pow(hashed_message, d, n)  # Signature: hash^d mod n
    print(f"  Original Message: {message}")
    print(f"  Hashed Message: {hashed_message}")
    print(f"  Signature: {signature}\n")

    # Verifying the signature
    print("Verifying the signature...")
    verified_hash = pow(signature, e, n)  # Verified hash: signature^e mod n
    print(f"  Verified Hash: {verified_hash}")
    print(f"  Hash Match: {hashed_message == verified_hash}")

    # Check if the signing and verification match
    if hashed_message == verified_hash:
        print("\nSignature and Verification Match! The process is successful.")
    else:
        print("\nSignature and Verification Failed! The process is unsuccessful.")

# Run the RSA signing and verification for strings
rsa_sign_and_verify()
