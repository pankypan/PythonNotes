# python高级(04)--多线程、多进程编程

## GIL

```python
# gil global interpreter lock （cpython）
# python中一个线程对应于c语言中的一个线程
# gil使得同一个时刻只有一个线程在一个cpu上执行字节码, 无法将多个线程映射到多个cpu上执行

# import dis
# def add(a):
#     a = a+1
#     return a
#
# print(dis.dis(add))  # 查看字节码


"""
GIL 的释放时机:
     gil会根据执行的字节码行数以及时间片(分时策略)释放 GIL
     GIL 在遇到 IO操作 时候主动释放
"""
import threading
total = 0


def add():
    # 1. dosomething1
    # 2. io操作
    # 1. dosomething3
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)  # 现象：total 不为0，说明 GIL 不是执行完一个线程结束后释放的
```



## 多线程编程

```python
# 对于io操作来说，多线程和多进程性能差别不大
import time
import threading


# 1.通过Thread类实例化
def get_detail_html(url):
    print("get detail html started", url)
    time.sleep(2)
    print("get detail html end", url)


def get_detail_url(url):
    print("get detail url started", url)
    time.sleep(4)
    print("get detail url end", url)


# 2. 通过继承Thread来实现多线程
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    # thread1 = threading.Thread(target=get_detail_html, args=('t1',))
    # thread2 = threading.Thread(target=get_detail_url, args=('t2',))
    thread1 = GetDetailHtml('t1')
    thread2 = GetDetailUrl('t2')

    # thread1.setDaemon(True)
    # thread2.setDaemon(True)

    start_time = time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    # 当主线程退出的时候， 子线程kill掉
    print('last time:', time.time() - start_time)
```



## 线程间通信

- 共享变量

使用一个全局变量, 然后不同线程可以访问并修改这个变量

- queue

```python
from queue import Queue

detail_url_queue = Queue(maxsize=1000)

queue.put("http://projectsedu.com/{id}".format(id=i))
url = queue.get()
```



## 线程同步

**(Lock,RLock,semaphores,Condition)**



**Lock&RLock:**

```python
import threading
from threading import Lock, RLock, Condition  # 可重入的锁

# 在同一个线程里面，可以连续调用多次acquire， 一定要注意acquire的次数要和release的次数相等
total = 0
lock = RLock()


def add():
    # 1. dosomething1
    # 2. io操作
    # 1. dosomething3
    global lock
    global total
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

#
thread1.join()
thread2.join()
print(total)

# 1. 用锁会影响性能
# 2. 锁会引起死锁
# 死锁的情况 A（a，b）
"""
A(a、b)
acquire (a)
acquire (b)

B(a、b)
acquire (b)
acquire (a)
"""
```



**Codition:**

```python
import threading


# 条件变量， 用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 好啊 ".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         self.lock.release()

# 通过condition完成协同读诗

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    from concurrent import futures

    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    xiaoai.start()
    tianmao.start()
```



**Semaphore:**

```python
# Semaphore 是用于控制进入数量的锁
# 文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个

# 做爬虫
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()

```





## 线程池编程

**concurrent**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future
from multiprocessing import Pool

# 未来对象，task的返回容器


# 线程池， 为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值
# 当一个线程完成的时候我们主线程能立即知道
# futures可以让多线程和多进程编码接口一致
import time


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中, submit 是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))


# 要获取已经成功的task的返回
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
# wait(all_task, return_when=FIRST_COMPLETED)
print("main")

# for future in as_completed(all_task):
#     data = future.result()
#     print("get {} page".format(data))

# 通过executor的map获取已经完成的task的值
# for data in executor.map(get_html, urls):
#     print("get {} page".format(data))


# #done方法用于判定某个任务是否完成
# print(task1.done())
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
#
# #result方法可以获取task的执行结果
# print(task1.result())

```



## 多线程与多进程对比

```python
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# 多进程编程
# 耗cpu的操作，用多进程编程， 对于io操作来说， 使用多线程编程，进程切换代价要高于线程

# 1. 对于耗费cpu的操作，多进程由于多线程
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)


# 2. 对于io操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    # 1. 对于耗费cpu的操作，多进程由于多线程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time() - start_time))

    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time() - start_time))

    # 2. 对于io操作来说，多线程优于多进程
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time() - start_time))

    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))
        print("last time is: {}".format(time.time() - start_time))

```



## 多进程编程

**multiprocessing**



## 进程间通信



