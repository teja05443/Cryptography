import socket

# Socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Receive public key from server
public_key = client_socket.recv(1024).decode()
e, n = map(int, public_key.split(','))

# User input for the plaintext message
user_string = input("Enter the message to encrypt (number): ")  # User inputs the plaintext number directly

# Convert to integer
plain_text = int(user_string)

# Send the plaintext message to the server
client_socket.sendall(str(plain_text).encode())

# Receive the encrypted message from the server
cipher_text = int(client_socket.recv(1024).decode())
print(f"Received Cipher Text: {cipher_text}")

# Close the connection
client_socket.close()
