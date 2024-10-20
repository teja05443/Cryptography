import socket

# Socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Input the plaintext message as a pair of integers
x_plaintext = int(input("Enter x-coordinate of the plaintext: "))
y_plaintext = int(input("Enter y-coordinate of the plaintext: "))
plaintext = (x_plaintext, y_plaintext)

# Send the plaintext to the server in the correct format
client_socket.sendall(f"{plaintext[0]},{plaintext[1]}".encode())

# Input the random integer K
k = int(input("Enter a random integer K: "))
client_socket.sendall(str(k).encode())  # Send K to the server

# Receive ciphertext from the server
ciphertext = client_socket.recv(1024).decode()
print(f"Received Cipher Text: {ciphertext}")

# Send ciphertext for decryption (for testing purposes, use the same ciphertext)
client_socket.sendall(ciphertext.encode())

# Close the connection
client_socket.close()
