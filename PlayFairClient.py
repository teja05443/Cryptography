import socket

def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Input plaintext message
    plaintext = input("Enter the plaintext message: ")
    
    client_socket.sendall(plaintext.encode())  # Send plaintext to server
    encrypted_text = client_socket.recv(1024).decode()  # Receive encrypted text

    print(f"Encrypted Text: {encrypted_text}")
    client_socket.close()

if __name__ == "__main__":
    start_client()