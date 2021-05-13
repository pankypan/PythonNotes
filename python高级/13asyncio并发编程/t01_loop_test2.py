import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return 'suki'

if __name__ == "__main__":
    # 获取协程的返回值
    # 1.使用 future 获取
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程内只有一个loop
    get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))
    loop.run_until_complete(get_future)
    print(get_future.result())
    print(time.time()-start_time)

    # 2.使用 task 获取
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程内只有一个loop
    task = loop.create_task(get_html("http://www.imooc.com"))
    loop.run_until_complete(task)
    print(task.result())
    print(time.time() - start_time)
