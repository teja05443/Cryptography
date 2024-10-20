import hmac
import hashlib
import socket

class HMACServer:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port

    def generate_hmac(self, secret_key, message):
        """Generate HMAC using SHA-512"""
        h = hmac.new(secret_key.encode(), message.encode(), hashlib.sha512)
        return h.hexdigest()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")

            try:
                # Receive key and message from client
                data = client_socket.recv(1024).decode()
                key, message = data.split('|')  # Assuming data format: "key|message"
                
                # Generate HMAC
                hmac_value = self.generate_hmac(key, message)
                
                response = f"HMAC: {hmac_value}"
                client_socket.send(response.encode())

            except Exception as e:
                print(f"Error: {e}")
                client_socket.send("Error processing request".encode())

            finally:
                client_socket.close()

if __name__ == "__main__":
    server = HMACServer()
    server.start()
