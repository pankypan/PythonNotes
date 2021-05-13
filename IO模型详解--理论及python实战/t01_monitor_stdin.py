import select
import sys


"""
注：
1、[sys.stdin,]以后不管是列表还是元组，在最后一个元素的后面建议增加一个逗号，（1，） | （1） 这两个有区别吗？是不是第二个更像方法的调用或者函数
    的调用，加个，是不是更容易分清楚。还有就是在以后写django的配置文件的时候，他是必须要加的。
2、select的第一个参数就是要监听的文件句柄，只要监听的文件句柄有变化，那么就会将其加入到返回值readable列表中。
3、select最后一个参数1是超时时间，当执行select时，如果监听的文件句柄没有变化，则会阻塞1秒，然后向下继续执行；默认timeout=None，
    就是会一直阻塞，直到感知到变化
"""


def monitor_stdin():
    while True:
        """
        select.select([sys.stdin,],[],[],1)用到I/O多路复用，第一个参数是列表，sys.stdin是系统标准输入的文件描述符, 就是打开标准输入终端返回
        的文件描述符，一旦终端有输入操作，select就感知sys.stdin描述符的变化，那么会将变化的描述符sys.stdin添加到返回值readable中；
        如果终端一直没有输入，那么readable他就是一个空列表
        """
        readable, writeable, error = select.select([sys.stdin, ], [], [])

        if sys.stdin in readable:
            print("select get stdin", sys.stdin.readline())


if __name__ == '__main__':
    monitor_stdin()
