# distributed_chat_client.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000  # Change to 5001 for server 2

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client,), daemon=True)
    receive_thread.start()

    while True:
        message = input()
        client.send(message.encode())

if __name__ == "__main__":
    main()
