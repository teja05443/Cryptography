import socket

def create_col_val(key):
    # Create a dictionary to store the order of key letters
    order = {int(val): num for num, val in enumerate(key)}
    return order

def encryption(no_rows, len_key, len_msg, msg, col_val):
    x = 0
    enc_mat = [[' ' for _ in range(len_key)] for _ in range(no_rows + 1)]

    # Fill the matrix with the message
    for i in range(no_rows + 1):
        for j in range(len_key):
            if x >= len_msg:
                enc_mat[i][j] = '_'
            else:
                enc_mat[i][j] = msg[x]
            x += 1

    # Construct the cipher text
    cipher = ''
    for t in range(1, len_key + 1):
        for i in range(len_key):
            k = col_val[i]
            if k == t:
                for j in range(no_rows + 1):
                    cipher += enc_mat[j][i]
                break

    return cipher

def decryption(no_rows, len_key, cipher, col_val):
    # Ensure the cipher text length matches the matrix size
    expected_length = (no_rows + 1) * len_key
    if len(cipher) < expected_length:
        cipher = cipher.ljust(expected_length, '_')

    dec_mat = [[' ' for _ in range(len_key)] for _ in range(no_rows + 1)]
    x = 0

    # Rearrange the matrix according to col_val
    for t in range(1, len_key + 1):
        for i in range(len_key):
            k = col_val[i]
            if k == t:
                for j in range(no_rows + 1):
                    if x < len(cipher):
                        dec_mat[j][i] = cipher[x]
                        x += 1
                break

    # Construct the original message
    message = ''
    for i in range(no_rows + 1):
        for j in range(len_key):
            if dec_mat[i][j] == '_':
                dec_mat[i][j] = ' '  # Replace '_' with space
            message += dec_mat[i][j]

    return message

def process_message(message, key, mode):
    len_key = len(key)
    len_msg = len(message)

    # Initialize col_val matrix
    col_val = [0] * len_key
    val = 1
    count = 0
    while count < len_key:
        min_val = 999
        for i in range(len_key):
            if min_val > ord(key[i]) and col_val[i] == 0:
                min_val = ord(key[i])
                ind = i
        col_val[ind] = val
        count += 1
        val += 1

    no_rows = len_msg // len_key + (1 if len_msg % len_key != 0 else 0)

    if mode == 'encrypt':
        return encryption(no_rows, len_key, len_msg, message, col_val)
    elif mode == 'decrypt':
        return decryption(no_rows, len_key, message, col_val)
    else:
        return "Invalid mode"

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

        mode, plaintext, key = data.split(';')
        result = process_message(plaintext, key, mode)

        client_socket.sendall(result.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
