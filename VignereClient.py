import socket

def send_message(host, port, plaintext, secret_key):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message_to_send = f"{plaintext};{secret_key}"
    client_socket.sendall(message_to_send.encode())
    print(f"Sent message: {message_to_send}")

    response = client_socket.recv(1024).decode()
    print(f"Received response: {response}")
    client_socket.close()

    return response

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    plaintext = "HELLO"
    secret_key = "KEY"

    encrypted_text = send_message(host, port, plaintext, secret_key)
    print(f"Encrypted text: {encrypted_text}")
