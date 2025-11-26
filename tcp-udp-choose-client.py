import socket
import threading

HOST = '127.0.0.1'
TCP_PORT = 5000
UDP_PORT = 5001

def receive_tcp(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

def receive_udp(client):
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            break

def main():
    choice = input("Choose protocol (tcp/udp): ").strip().lower()
    if choice == "tcp":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, TCP_PORT))
        threading.Thread(target=receive_tcp, args=(client,), daemon=True).start()
        while True:
            message = input()
            client.send(message.encode())
    elif choice == "udp":
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        threading.Thread(target=receive_udp, args=(client,), daemon=True).start()
        while True:
            message = input("Enter message: ")
            client.sendto(message.encode(), (HOST, UDP_PORT))
    else:
        print("Invalid choice. Exiting.")
        return

if __name__ == "__main__":
    main()
