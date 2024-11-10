# bob_server.py
import socket
import random
from dh_config import DH_PRIME, DH_BASE, BOB_HOST, BOB_PORT

def start_server():
    # DH parameters
    p = DH_PRIME
    g = DH_BASE
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((BOB_HOST, BOB_PORT))
        server_socket.listen(1)
        print(f"Bob's server started on {BOB_HOST}:{BOB_PORT}")
        
        while True:
            client_socket, address = server_socket.accept()
            try:
                print(f"Connection from: {address}")
                
                # Generate Bob's private and public keys
                bob_private_key = random.randint(1, p-1)
                bob_public_key = pow(g, bob_private_key, p)
                
                # Receive "Alice's" public key (actually from Darth)
                received_public_key = int(client_socket.recv(1024).decode())
                print(f"Received public key: {received_public_key}")
                
                # Send Bob's public key
                client_socket.send(str(bob_public_key).encode())
                
                # Calculate shared secret
                shared_secret = pow(received_public_key, bob_private_key, p)
                print(f"Bob's calculated shared secret: {shared_secret}")
                
            except Exception as e:
                print(f"Error handling connection: {e}")
            finally:
                client_socket.close()
                
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()