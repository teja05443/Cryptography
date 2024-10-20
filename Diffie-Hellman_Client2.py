import socket
import random

def generate_private_key(lim):
    return random.randint(1, lim - 1)

def generate_public_key(gen, privkey, lim):
    return pow(gen, privkey, lim)

def main():
    lim = 23  # Prime number
    gen = 5   # Generator

    # Generate private and public keys for Client 2 (Bob)
    bobprivkey = generate_private_key(lim)
    bobpubkey = generate_public_key(gen, bobprivkey, lim)

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Send public key to the server
    client_socket.send(str(bobpubkey).encode())

    # Receive public key from Client 1 (Alice)
    alpubkey = int(client_socket.recv(1024).decode())

    # Compute the shared secret key
    bobshrkey = pow(alpubkey, bobprivkey, lim)

    print(f"Client 2 - Bob's Private Key: {bobprivkey}")
    print(f"Client 2 - Bob's Public Key: {bobpubkey}")
    print(f"Received Client 1 (Alice's) Public Key: {alpubkey}")
    print(f"Shared Secret Key: {bobshrkey}")

    # Simulate receiving the encrypted message from Client 1
    encrypted = 12 * bobshrkey  # Assuming the encrypted message from Alice
    decrypted = encrypted / bobshrkey
    print(f"Decrypted message: {int(decrypted)}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
