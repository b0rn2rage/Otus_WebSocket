import socket
from task1.config import LOCALHOST, random_port

BACKLOG = 10

my_socket = socket.socket()
address_and_port = (LOCALHOST, random_port())
my_socket.bind(address_and_port)

print("Socket bind on =", address_and_port)

my_socket.listen(BACKLOG)

conn, address = my_socket.accept()

# При подключении возвращает параметры соединения и адрес клиента
print("connection:", conn)
print("address:", address)

# Получаем данные из соединения
data = conn.recv(1024)

conn.send(
    f"HTTP/1.1 200 OK\r\n Content-Length: 100\r\n Connection: close\r\n Content-Type: text/html\r\n\n "
    f"<h3>{data.decode()}</h3>".encode("utf-8"))
my_socket.close()
