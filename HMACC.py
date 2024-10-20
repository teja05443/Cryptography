import socket

class HMACClient:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port

    def send_message(self, key, message):
        """Send key and message to the server"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))

        # Send key|message to the server
        client_socket.send(f"{key}|{message}".encode())

        # Receive and print response from the server
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

        client_socket.close()

if __name__ == "__main__":
    client = HMACClient()

    # Input key and message
    key = input("Enter the secret key: ")
    message = input("Enter a message to send: ")
    client.send_message(key, message)
