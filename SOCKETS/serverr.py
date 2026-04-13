import socket
server=socket.socket()
server.bind(('localhost',12345))
server.listen(1)
print("server waiting for connection...")
conn,addr=server.accept()
print("connected with",addr)