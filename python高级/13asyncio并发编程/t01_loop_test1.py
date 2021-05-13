"""
事件循环+回调（驱动生成器）+epoll(IO多路复用)
asyncio是python用于解决异步io编程的一整套解决方案
tornado、gevent、twisted（scrapy， django channels） 基于asyncio
torando(实现web服务器)， tornado可以直接部署， nginx+tornado， 而
django/flask没有实现web服务器，需要添加其他组件(uwsgi, gunicorn+nginx)完成部署
"""
import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")

if __name__ == "__main__":
    # 使用asyncio
    # 1.执行单个任务
    start_time = time.time()
    loop1 = asyncio.get_event_loop()  # 一个线程内只有一个loop
    task = loop1.create_task(get_html("www.baidu.com"))
    loop1.run_until_complete(task)
    print(time.time() - start_time)

    # 2.执行多个任务
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程内只有一个loop
    tasks = [get_html("http://www.imooc.com") for _ in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start_time)

    print(loop1 is loop)  # True 一个线程内只有一个loop

