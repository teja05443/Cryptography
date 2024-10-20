import socket

def send_message(host, port, mode, plaintext, key):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message_to_send = f"{mode};{plaintext};{key}"
    client_socket.sendall(message_to_send.encode())
    print(f"Sent message: {message_to_send}")

    response = client_socket.recv(1024).decode()
    print(f"Received response: {response}")
    client_socket.close()

    return response

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    mode = 'encrypt'  # or 'decrypt'
    plaintext = "Geeks for Geeks"
    key = "HACK"

    response = send_message(host, port, mode, plaintext, key)
    print(f"Response: {response}")

    # For decryption
    mode = 'decrypt'
    cipher_text = response  # Use the response from the encryption as the cipher text

    response = send_message(host, port, mode, cipher_text, key)
    print(f"Decrypted text: {response}")
