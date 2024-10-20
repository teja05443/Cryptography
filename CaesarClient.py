import socket

def send_message(host, port, message, shift):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message_to_send = f"{message};{shift}"
    client_socket.sendall(message_to_send.encode())

    response = client_socket.recv(1024).decode()
    client_socket.close()

    return response

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    plaintext = "Hello, World!"
    shift_amount = 3

    encrypted_text = send_message(host, port, plaintext, shift_amount)
    print(f"Encrypted text: {encrypted_text}")
