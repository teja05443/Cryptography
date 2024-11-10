# darth_mitm.py
import socket
import random
from dh_config import DH_PRIME, DH_BASE, BOB_HOST, BOB_PORT, DARTH_HOST, DARTH_PORT

def start_mitm():
    # DH parameters
    p = DH_PRIME
    g = DH_BASE
    
    # Create MITM server socket
    mitm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mitm_socket.bind((DARTH_HOST, DARTH_PORT))
        mitm_socket.listen(1)
        print(f"Darth's MITM server started on {DARTH_HOST}:{DARTH_PORT}")
        
        while True:
            # Accept connection from Alice
            alice_socket, address = mitm_socket.accept()
            try:
                print(f"Connection from Alice: {address}")
                
                # Generate Darth's private and public keys
                darth_private_key = random.randint(1, p-1)
                darth_public_key = pow(g, darth_private_key, p)
                
                # Receive Alice's public key
                alice_public_key = int(alice_socket.recv(1024).decode())
                print(f"Intercepted Alice's public key: {alice_public_key}")
                
                # Connect to Bob
                bob_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    bob_connection.connect((BOB_HOST, BOB_PORT))
                    
                    # Forward Darth's public key to Bob (instead of Alice's)
                    bob_connection.send(str(darth_public_key).encode())
                    
                    # Receive Bob's public key
                    bob_public_key = int(bob_connection.recv(1024).decode())
                    print(f"Intercepted Bob's public key: {bob_public_key}")
                    
                    # Send Darth's public key to Alice (instead of Bob's)
                    alice_socket.send(str(darth_public_key).encode())
                    
                    # Calculate shared secrets
                    shared_secret_with_alice = pow(alice_public_key, darth_private_key, p)
                    shared_secret_with_bob = pow(bob_public_key, darth_private_key, p)
                    
                    print(f"Darth's shared secret with Alice: {shared_secret_with_alice}")
                    print(f"Darth's shared secret with Bob: {shared_secret_with_bob}")
                    
                finally:
                    bob_connection.close()
                    
            except Exception as e:
                print(f"Error handling connection: {e}")
            finally:
                alice_socket.close()
                
    except Exception as e:
        print(f"MITM server error: {e}")
    finally:
        mitm_socket.close()

if __name__ == "__main__":
    start_mitm()