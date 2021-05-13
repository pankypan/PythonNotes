import asyncio
import time

"""
# 1. run_until_complete
loop = asyncio.get_event_loop()
loop.run_forever()
loop.run_until_complete()
"""


async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)
    print(f"done after {sleep_times} s")


if __name__ == '__main__':
    # 运行过程中，取消task
    task1 = get_html(5)
    task2 = get_html(10)
    task3 = get_html(15)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:  # 使用 ctrl + c时，取消task
        print(e)
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
