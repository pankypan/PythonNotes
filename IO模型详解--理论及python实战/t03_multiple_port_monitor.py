import socket
import select


def browser_monitor():
    # 生成socket对象
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口
    sk.bind(('0.0.0.0', 8000))
    # 监听，并设置最大连接数为5
    sk.listen(5)
    # 设置setblocking为False，即非阻塞模式，accept将不在阻塞，如果没有收到请求就会报错
    sk.setblocking(False)

    sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk2.bind(('0.0.0.0', 8006))
    sk2.listen(5)
    sk2.setblocking(False)

    while True:
        rlist, wlist, elist = select.select([sk, sk2], [], [], 2)  # 监听第一个列表的文件描述符，如果其中有文件描述符发生改变，则捕获并放到rlist中
        for r in rlist:  # 如果rlist非空将执行，否则不执行
            conn, addr = r.accept()  # 建立连接，生成客户端的socket对象以及IP地址和端口号
            print(addr)


if __name__ == '__main__':
    browser_monitor()
