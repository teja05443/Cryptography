import socket
import random

# S-box and Inverse S-box for substitution
sbox = [0x0, 0xf, 0x1, 0xe, 0x2, 0xd, 0x3, 0xc, 0x4, 0xb, 0x5, 0xa, 0x6, 0x9, 0x7, 0x8]
invsbox = [0 for i in range(16)]
for i in range(16):
    invsbox[sbox[i]] = i

# Utility functions
def binary(n):
    A = []
    a = n
    for i in range(4):
        x = a % 2
        A.append(x)
        a = int((a - x) / 2)
    B = [A[3 - i] for i in range(4)]
    return B

def integer(l):
    a = 0
    for i in range(len(l)):
        a += l[i] * (2 ** (len(l) - i - 1))
    return a

def xor(arr1, arr2):
    temp = []
    for i in range(len(arr1)):
        temp.append(arr1[i] ^ arr2[i])
    return temp

def subbytes(S):
    T = [0 for i in range(8)]
    for i in range(2):
        a = 0
        for j in range(4):
            a += S[4 * i + j] * (2 ** (3 - j))
        A = binary(sbox[a])
        for j in range(4):
            T[4 * i + j] = A[j]
    return T

def invsubbytes(S):
    T = [0 for i in range(8)]
    for i in range(2):
        a = 0
        for j in range(4):
            a += S[4 * i + j] * (2 ** (3 - j))
        A = binary(invsbox[a])
        for j in range(4):
            T[4 * i + j] = A[j]
    return T

def matrixsplitter(C):
    Matrix = []
    for i in range(2):
        temp = []
        for j in range(4):
            temp.append(C[i * 4 + j])
        Matrix.append(temp)
    return Matrix

def matrixcombiner(Matrix):
    temp = []
    for i in range(2):
        for j in range(4):
            temp.append(Matrix[i][j])
    return temp

def rotate(row, places, direction):
    n = len(row)
    if direction == 1:  # Rotate left
        return row[places % n:] + row[:places % n]
    elif direction == -1:  # Rotate right
        return row[-places % n:] + row[:-places % n]
    return 0

def Shiftrows(Matrix):
    for i in range(2):
        Matrix[i] = rotate(Matrix[i], 1, 1)
    return Matrix

def InverseShiftrows(Matrix):
    for i in range(2):
        Matrix[i] = rotate(Matrix[i], 1, -1)
    return Matrix

def Encrypt(P):
    C = subbytes(P)
    C1 = Shiftrows(matrixsplitter(C))
    return matrixcombiner(C1)

def Decrypt(C):
    C1 = InverseShiftrows(matrixsplitter(C))
    C2 = invsubbytes(matrixcombiner(C1))
    return C2

# Helper functions to convert between text and binary
def text_to_binary(text):
    binary_text = []
    for char in text:
        bin_value = format(ord(char), '08b')
        binary_text.extend([int(bit) for bit in bin_value])
    return binary_text

def binary_to_text(binary):
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        byte_value = int(''.join(map(str, byte)), 2)
        text += chr(byte_value)
    return text

def handle_client(conn):
    # Receive plaintext and key from client
    data = conn.recv(1024).decode()
    if not data:
        return
    data = data.split(',')
    input_text = data[0].strip()
    input_key = data[1].strip()

    # Determine if input is binary or text
    if all(c in '01' for c in input_text):  # Binary input
        Plain_Text = [int(bit) for bit in input_text]
        Key = [int(bit) for bit in input_key]
    else:  # Text input
        Plain_Text = text_to_binary(input_text)
        Key = text_to_binary(input_key)

    # Encryption/Decryption in blocks of 8 bits
    Cipher = []
    Decrypted_Text = []
    
    for i in range(0, len(Plain_Text), 8):
        P_block = Plain_Text[i:i+8]
        K_block = Key[:8]  # Using first 8 bits of the key

        # Encryption
        Cipher_block = Encrypt(P_block)
        Round_Key = Encrypt(K_block)
        Cipher_block = xor(Cipher_block, Round_Key)

        Cipher.extend(Cipher_block)

        # Decryption
        Decrypted_block = xor(Cipher_block, Round_Key)
        Decrypted_block = Decrypt(Decrypted_block)
        Decrypted_Text.extend(Decrypted_block)

    # Convert back to text if input was text
    if all(c in '01' for c in input_text):
        decrypted_message = f"Decrypted Binary: {''.join([str(bit) for bit in Decrypted_Text])}"
    else:
        decrypted_message = f"Decrypted Text: {binary_to_text(Decrypted_Text)}"

    response = f"Cipher: {''.join([str(bit) for bit in Cipher])}, {decrypted_message}"
    conn.send(response.encode())

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 65432))
    server.listen(1)
    print("Server is listening...")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        handle_client(conn)
        conn.close()

if __name__ == "__main__":
    start_server()
