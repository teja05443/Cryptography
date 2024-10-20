import socket

def request_sha512(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Send message to the server
    client_socket.send(message.encode())
    
    # Receive SHA-512 hash from the server
    response = client_socket.recv(1024).decode()
    print(f"SHA-512 hash of '{message}' is: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    message = input("Enter the message to hash: ")
    request_sha512(message)