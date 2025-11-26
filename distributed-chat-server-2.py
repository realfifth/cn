# distributed_chat_server2.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5001
PEER_PORT = 5000

clients = []
peer_server = None

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def forward_to_peer(message):
    try:
        peer_server.send(message.encode())
    except:
        pass

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"Received: {message}")
                broadcast(message, client)
                forward_to_peer(message)
        except:
            clients.remove(client)
            client.close()
            break

def peer_listener():
    global peer_server
    peer_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_server.connect((HOST, PEER_PORT))
    while True:
        try:
            message = peer_server.recv(1024).decode()
            if message:
                print(f"From peer: {message}")
                broadcast(message, None)
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Distributed Chat Server 2 running...")

    threading.Thread(target=peer_listener, daemon=True).start()

    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f"Connected: {addr}")
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()
