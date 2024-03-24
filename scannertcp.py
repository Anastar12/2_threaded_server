import socket

target_ip = input("Введите имя хоста/IP-адрес: ")

start_port = 0
end_port = 2**16 - 1

for port in range(start_port, end_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Порт {port} открыт")
    sock.close()
