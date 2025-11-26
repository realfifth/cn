# weather_client.py
import socket

HOST = '127.0.0.1'
PORT = 5000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip().lower()
        if city == 'quit':
            break
        client.send(city.encode())
        response = client.recv(1024).decode()
        print(f"Weather for {city}: {response}")

    client.close()

if __name__ == "__main__":
    main()
