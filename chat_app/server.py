# server.py
import socket

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# fix port issue
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind
server_socket.bind(("localhost", 9999))

# listen
server_socket.listen(1)
print("Server started... Waiting for client...")

# accept
conn, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    # receive message
    data = conn.recv(1024).decode()

    if data.lower() == "exit":
        print("Client disconnected")
        break

    print("Client:", data)

    # send reply
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
server_socket.close()