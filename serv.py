import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
data = conn.recv(512).decode()
conn.send(data.upper().encode())
