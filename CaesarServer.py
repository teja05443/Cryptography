import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024).decode()
        if not data:
            break

        plaintext, shift_amount = data.split(';')
        shift_amount = int(shift_amount)
        encrypted_text = caesar_cipher(plaintext, shift_amount)

        client_socket.sendall(encrypted_text.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
