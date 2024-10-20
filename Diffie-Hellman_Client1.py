import socket
import random

def generate_private_key(lim):
    return random.randint(1, lim - 1)

def generate_public_key(gen, privkey, lim):
    return pow(gen, privkey, lim)

def main():
    lim = 23  # Prime number
    gen = 5   # Generator

    # Generate private and public keys for Client 1 (Alice)
    alprivkey = generate_private_key(lim)
    alpubkey = generate_public_key(gen, alprivkey, lim)

    # Connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Send public key to the server
    client_socket.send(str(alpubkey).encode())

    # Receive public key from Client 2 (Bob)
    bobpubkey = int(client_socket.recv(1024).decode())

    # Compute the shared secret key
    alshrkey = pow(bobpubkey, alprivkey, lim)

    print(f"Client 1 - Alice's Private Key: {alprivkey}")
    print(f"Client 1 - Alice's Public Key: {alpubkey}")
    print(f"Received Client 2 (Bob's) Public Key: {bobpubkey}")
    print(f"Shared Secret Key: {alshrkey}")

    # Encrypt a message using the shared secret key
    msg = 12
    encrypted = msg * alshrkey
    print(f"Encrypted message: {encrypted}")

    # Simulate sending the encrypted message to Client 2 and receiving the decrypted message
    decrypted = encrypted / alshrkey
    print(f"Decrypted message: {int(decrypted)}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
