import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 65432))

    # Input plaintext and key (binary or letters)
    plaintext = input("Enter plaintext (letters or binary): ").strip()
    key = input("Enter key (letters or binary): ").strip()

    # Send data to server
    client.send(f"{plaintext},{key}".encode())

    # Receive and print the response from the server
    response = client.recv(1024).decode()
    print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    start_client()
