import socket
import threading

HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001

tcp_clients = []
udp_clients = []

def broadcast_tcp(message, sender):
    for client in tcp_clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                tcp_clients.remove(client)

def handle_tcp_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"TCP: {message}")
                broadcast_tcp(message, client)
        except:
            tcp_clients.remove(client)
            client.close()
            break

def broadcast_udp(message, sender):
    for client in udp_clients:
        if client != sender:
            udp_server.sendto(message.encode(), client)

def udp_server_loop():
    while True:
        message, addr = udp_server.recvfrom(1024)
        print(f"UDP: {message.decode()}")
        if addr not in udp_clients:
            udp_clients.append(addr)
        broadcast_udp(message.decode(), addr)

def main():
    global udp_server
    
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind((HOST, TCP_PORT))
    tcp_server.listen()
    print("Combined Chat Server running...")

    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_server.bind((HOST, UDP_PORT))
    threading.Thread(target=udp_server_loop, daemon=True).start()


    while True:
        client, addr = tcp_server.accept()
        tcp_clients.append(client)
        print(f"TCP client connected: {addr}")
        threading.Thread(target=handle_tcp_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    main()
