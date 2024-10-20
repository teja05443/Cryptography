import socket

def create_playfair_matrix():
    """Creates a Playfair matrix using the alphabet without 'J'."""
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # J is replaced by I
    matrix = []
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return matrix

def preprocess_text(text):
    """Prepares the text for encryption by replacing J with I and ensuring even length."""
    text = text.upper().replace('J', 'I').replace(' ', '')
    result = ''
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += text[i] + 'X'  # Insert 'X' between duplicate letters
            i += 1
        else:
            result += text[i]
            i += 1
    if len(result) % 2 != 0:
        result += 'X'  # Append 'X' if odd length
    return result

def encrypt_playfair(plaintext):
    """Encrypts plaintext using the Playfair cipher."""
    matrix = create_playfair_matrix()
    plaintext = preprocess_text(plaintext)
    ciphertext = ''
    
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i + 2]
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)

        if row1 == row2:
            # Same row: Shift right
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5]
            ciphertext += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            # Same column: Shift down
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            # Rectangle: Swap columns
            ciphertext += matrix[row1 * 5 + col2]
            ciphertext += matrix[row2 * 5 + col1]
    
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

        plaintext = data.strip()  # Receive only the plaintext
        encrypted_text = encrypt_playfair(plaintext)

        client_socket.sendall(encrypted_text.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
