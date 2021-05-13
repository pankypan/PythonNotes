import socket
import select
import time


def server():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('0.0.0.0', 8000))
    sk.listen(5)
    sk.setblocking(False)
    inputs = [sk, ]

    while True:
        rlist, wlist, elist = select.select(inputs, [], [], 1)
        time.sleep(2)
        print("inputs list:", inputs)
        print("file descriptor:", rlist)

        for r in rlist:
            if r == sk:
                # 当客户端第1次连接服务端时
                conn, address = r.accept()
                inputs.append(conn)
                print(address)
            else:
                # 当客户端连接上服务端之后，再次发送数据时
                client_data = r.recv(1024)
                r.sendall(client_data)


if __name__ == '__main__':
    server()
