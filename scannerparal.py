import concurrent.futures
import socket
from tqdm import tqdm

PORTS = []

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        PORTS.append(port)   
    except socket.error:
        pass

def main():
    target_ip = input("Введите имя хоста/IP-адрес: ")
    ports = range(0, 2**16 - 1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(scan_port, target_ip, port) for port in ports]
        for future in tqdm(concurrent.futures.as_completed(futures)):
            future.result()
    PORTS.sort()
    for port in PORTS:
        print(f"Порт {port} открыт")



if __name__ == '__main__':
    main()
