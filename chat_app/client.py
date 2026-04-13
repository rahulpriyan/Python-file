# client.py
import socket

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client_socket.connect(("localhost", 9999))
print("Connected to server")

while True:
    # send message
    msg = input("You: ")
    client_socket.send(msg.encode())

    if msg.lower() == "exit":
        break

    # receive reply
    data = client_socket.recv(1024).decode()
    print("Server:", data)

client_socket.close()