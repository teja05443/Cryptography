import socket

def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            shifted_char = chr(((ord(plain_text[i].upper()) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

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

        plaintext, secret_key = data.split(';')
        encrypted_text = vigenere_encrypt(plaintext, secret_key)

        client_socket.sendall(encrypted_text.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
