import socket
import random

def generate_random_bits(size):
    return [random.randint(0, 1) for _ in range(size)]

def send_data(sock, data):
    sock.send(bytes(data))

def receive_data(sock, size):
    return list(sock.recv(size))

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    
    Plain_Text = generate_random_bits(128)
    Key = generate_random_bits(128)

    
    send_data(client_socket, Plain_Text)
    send_data(client_socket, Key)

    
    encrypted_data = receive_data(client_socket, 128)

    
    decrypted_data = receive_data(client_socket, 128)

    print("Plain Text:", Plain_Text)
    print("Cipher Text:", encrypted_data)
    print("Decrypted Text:", decrypted_data)

    client_socket.close()

if __name__ == "__main__":
    main()
