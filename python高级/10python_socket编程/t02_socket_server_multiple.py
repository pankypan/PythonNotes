import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(10)


def handle_sock(sock: socket.socket, addr):
    while True:
        print('new sock', sock, addr)
        recv_data = sock.recv(1024).decode('utf-8')
        print(recv_data)
        if recv_data == 'Q':
            break
        re_data = input()
        sock.send(re_data.encode('utf-8'))
    sock.close()


# 获取从客户端发送的数据
# 一次获取1k的数据
while True:
    sock, addr = server.accept()  # 阻塞

    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()

# sock.close()
# server.close()
