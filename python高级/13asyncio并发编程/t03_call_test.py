import asyncio


def callback(sleep_times):
    print("success time {}".format(sleep_times))


def callback_2(name, loop):
    print("{} success time {}".format(name, loop.time()))


def stop_loop(loop):
    loop.stop()


# call_later, call_at
if __name__ == "__main__":
    # call_soon & call_later
    loop = asyncio.get_event_loop()

    # 1.call_later
    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)

    # 2.call_soon
    loop.call_soon(callback, 4)

    # 3.call_at
    now = loop.time()
    print('loop now time:', now)
    loop.call_at(now + 2, callback_2, 'c2', loop)
    loop.call_at(now + 1, callback_2, 'c1', loop)
    loop.call_at(now + 3, callback_2, 'c3', loop)

    # loop.call_soon(stop_loop, loop)
    loop.run_forever()
