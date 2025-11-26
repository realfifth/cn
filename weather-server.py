# weather_server.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

# Simulated weather data
weather_data = {
    "mangalore": "Temperature: 28°C, Humidity: 75%, Condition: Sunny",
    "bangalore": "Temperature: 22°C, Humidity: 60%, Condition: Cloudy",
    "delhi": "Temperature: 35°C, Humidity: 40%, Condition: Hot",
    "mumbai": "Temperature: 30°C, Humidity: 80%, Condition: Rainy",
}

def handle_client(client):
    while True:
        try:
            city = client.recv(1024).decode().strip().lower()
            if city in weather_data:
                response = weather_data[city]
            else:
                response = "Weather data not available for this city."
            client.send(response.encode())
        except:
            break
    client.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Weather Server running...")

    while True:
        client, addr = server.accept()
        print(f"Connected from {addr}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()
