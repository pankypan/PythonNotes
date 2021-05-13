import socket


def run_client():
    client = socket.socket()
    client.connect(('127.0.0.1', 8000))
    client.settimeout(5)

    while True:
        client_input = input("please input message:").strip()
        client.sendall(client_input.encode('utf-8'))
        server_data = client.recv(1024)
        print(server_data)


if __name__ == '__main__':
    run_client()
