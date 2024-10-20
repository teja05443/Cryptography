import socket

def rail_fence_encrypt(plain_text, key):
    # Initialize the grid
    enc = [["" for _ in range(len(plain_text))] for _ in range(key)]

    # Fill the grid with characters
    flag, row = 0, 0
    for i in range(len(plain_text)):
        enc[row][i] = plain_text[i]
        if flag == 0:
            row += 1
            if row == key:
                flag = 1
                row -= 2
        else:
            row -= 1
            if row == -1:
                flag = 0
                row += 2

    # Read the ciphertext row by row
    ciphertext = "".join("".join(row) for row in enc if row)
    return ciphertext

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

        plaintext, key = data.split(';')
        key = int(key)
        encrypted_text = rail_fence_encrypt(plaintext, key)

        client_socket.sendall(encrypted_text.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
