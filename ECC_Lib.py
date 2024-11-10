from tinyec import registry
from Cryptodome.Random import get_random_bytes
import secrets

def ecc_point_to_bytes(point):
    return point.x.to_bytes(32, 'big') + point.y.to_bytes(32, 'big')

def encrypt_ecc(msg, pubKey):
    ciphertext_privKey = secrets.randbelow(curve.field.n)
    shared_key = ciphertext_privKey * pubKey
    
    # Convert shared key to bytes
    shared_key_bytes = ecc_point_to_bytes(shared_key)
    
    # Use shared key bytes for encryption (in practice, use proper KDF)
    from Cryptodome.Cipher import AES
    from Cryptodome.Util.Padding import pad
    
    cipher = AES.new(shared_key_bytes[:32], AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(msg, AES.block_size))
    
    return (ciphertext_privKey * curve.g, cipher.iv, ciphertext)

def decrypt_ecc(encrypted_msg, privKey):
    shared_key = privKey * encrypted_msg[0]
    shared_key_bytes = ecc_point_to_bytes(shared_key)
    
    from Cryptodome.Cipher import AES
    from Cryptodome.Util.Padding import unpad
    
    cipher = AES.new(shared_key_bytes[:32], AES.MODE_CBC, encrypted_msg[1])
    plaintext = unpad(cipher.decrypt(encrypted_msg[2]), AES.block_size)
    return plaintext

def ecc_example():
    # Get standard named curve
    global curve
    curve = registry.get_curve('brainpoolP256r1')

    # Generate private key
    privKey = secrets.randbelow(curve.field.n)
    # Generate public key
    pubKey = privKey * curve.g

    # Original message
    msg = b'This is a secret message for ECC encryption'
    print("Original message:", msg.decode())

    # Encrypt message
    encrypted = encrypt_ecc(msg, pubKey)
    print("Encrypted message (showing first 32 bytes):", encrypted[2][:32].hex())

    # Decrypt message
    decrypted = decrypt_ecc(encrypted, privKey)
    print("Decrypted message:", decrypted.decode())

print("\n=== ECC Encryption/Decryption ===")
ecc_example()