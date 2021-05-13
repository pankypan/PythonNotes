import asyncio
import time
from functools import partial


async def get_html(url):
    print(f"start get url: {url}")
    await asyncio.sleep(2)
    print(f"end get url: {url}")
    return 'suki'


if __name__ == "__main__":
    # wait 和 gather
    # 1.使用 wait
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程内只有一个loop
    tasks = [get_html("www.baidu.com") for _ in range(5)]
    loop.run_until_complete(asyncio.wait(tasks))  # 使用 wait
    print(time.time()-start_time)

    # 2.使用 gather
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 一个线程内只有一个loop
    tasks = [get_html("www.jd.com") for _ in range(5)]
    loop.run_until_complete(asyncio.gather(*tasks))  # 使用 gather
    print(time.time()-start_time)

    # 3.gather 和 wait 的区别，gather 更加 high-level，gather 可以分组
    start_time = time.time()
    group1 = [get_html('www.google.com') for _ in range(2)]
    group2 = [get_html('www.youtube.com') for _ in range(2)]
    loop.run_until_complete(asyncio.gather(*group1, *group2))
    # group1 = asyncio.gather(*group1)
    # group2 = asyncio.gather(*group2)
    # loop.run_until_complete(asyncio.gather(group1, group2))
    # group1.cancel()
    print(time.time()-start_time)
