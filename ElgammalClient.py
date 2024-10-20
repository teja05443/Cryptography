import socket

# Socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Input values for q, alpha, and xa
q = int(input("Enter a prime number q: "))
alpha = int(input("Enter a primitive root alpha of q: "))
xa = int(input("Enter the private key xa: "))

# Send q, alpha, and xa to the server
client_socket.sendall(f"{q},{alpha},{xa}".encode())

# Input the plaintext message M and random integer K
M = int(input("Enter the plaintext message M (as an integer): "))
K = int(input("Enter a random integer K: "))

# Send the plaintext message and K to the server
client_socket.sendall(f"{M},{K}".encode())

# Receive ciphertext from the server
cipher_text = client_socket.recv(1024).decode()
print(f"Received Cipher Text: {cipher_text}")

# Send ciphertext for decryption
client_socket.sendall(cipher_text.encode())

# Close the connection
client_socket.close()
