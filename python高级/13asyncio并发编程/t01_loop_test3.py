import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return 'suki'


def callback(future):
    print("send email to suki!")


def callback_with_para(name, future):
    print(f"{name} completed task!")


if __name__ == "__main__":
    # 执行回调函数
    start_time = time.time()
    loop = asyncio.get_event_loop()
    task = loop.create_task(get_html("http://www.imooc.com"))
    # 1.不带参数的callback
    task.add_done_callback(callback)
    # 2.携带参数的callback
    task.add_done_callback(partial(callback_with_para, 'snoopy'))
    loop.run_until_complete(task)
    print('result:', task.result())
    print(time.time() - start_time)
