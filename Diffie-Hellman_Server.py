import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)

    print("Server is waiting for connections...")

    # Accept connection from client 1
    client1, addr1 = server_socket.accept()
    print(f"Client 1 connected from {addr1}")

    # Accept connection from client 2
    client2, addr2 = server_socket.accept()
    print(f"Client 2 connected from {addr2}")

    # Receive public key from client 1
    client1_pubkey = client1.recv(1024).decode()
    print(f"Received public key from Client 1: {client1_pubkey}")

    # Receive public key from client 2
    client2_pubkey = client2.recv(1024).decode()
    print(f"Received public key from Client 2: {client2_pubkey}")

    # Send public key of Client 2 to Client 1
    client1.send(client2_pubkey.encode())
    print(f"Sent public key of Client 2 to Client 1")

    # Send public key of Client 1 to Client 2
    client2.send(client1_pubkey.encode())
    print(f"Sent public key of Client 1 to Client 2")

    # Close connections
    client1.close()
    client2.close()
    server_socket.close()

if __name__ == "__main__":
    main()
