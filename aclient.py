# alice_client.py
import socket
import random
from dh_config import DH_PRIME, DH_BASE, DARTH_HOST, DARTH_PORT

def start_client():
    # DH parameters
    p = DH_PRIME
    g = DH_BASE
    
    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to what Alice thinks is Bob's server (actually Darth's MITM server)
        client_socket.connect((DARTH_HOST, DARTH_PORT))
        print(f"Connected to server at {DARTH_HOST}:{DARTH_PORT}")
        
        # Generate Alice's private and public keys
        alice_private_key = random.randint(1, p-1)
        alice_public_key = pow(g, alice_private_key, p)
        print(f"Alice's public key: {alice_public_key}")
        
        # Send Alice's public key
        client_socket.send(str(alice_public_key).encode())
        
        # Receive "Bob's" public key (actually from Darth)
        received_public_key = int(client_socket.recv(1024).decode())
        print(f"Received public key: {received_public_key}")
        
        # Calculate shared secret
        shared_secret = pow(received_public_key, alice_private_key, p)
        print(f"Alice's calculated shared secret: {shared_secret}")
        
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()