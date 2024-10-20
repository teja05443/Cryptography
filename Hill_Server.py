import socket
import numpy as np

def create_key_matrix():
    """Creates a hardcoded key matrix for encryption."""
    return np.array([
        [17, 17, 5],
        [21, 18, 21],
        [2, 2, 19]
    ], dtype=int)

def preprocess_text(plaintext, block_size):
    """Prepares the text for encryption by padding if necessary."""
    plaintext = plaintext.replace(' ', '').upper()
    while len(plaintext) % block_size != 0:  # Pad with 'X' if not divisible by block size
        plaintext += 'X'
    return plaintext

def encrypt_hill(plaintext, key_matrix):
    """Encrypts plaintext using the Hill cipher."""
    block_size = key_matrix.shape[0]
    plaintext = preprocess_text(plaintext, block_size)
    ciphertext = ''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        block_vector = np.array([ord(char) - ord('A') for char in block])  # Convert to integer vector
        encrypted_block = np.dot(key_matrix, block_vector) % 26  # Perform matrix multiplication and modulo
        ciphertext += ''.join(chr(num + ord('A')) for num in encrypted_block)  # Convert back to characters

    return ciphertext

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode()
        if not data:
            break

        plaintext = data  # Get plaintext from client
        key_matrix = create_key_matrix()  # Use predefined key matrix
        encrypted_text = encrypt_hill(plaintext, key_matrix)

        client_socket.sendall(encrypted_text.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
