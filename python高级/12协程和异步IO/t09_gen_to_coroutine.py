# 生成器是可以暂停的函数
import inspect


# 1. 用同步的方式编写异步的代码， 在适当的时候暂停函数并在适当的时候启动函数
def gen_func():
    value = yield 1
    # 第一返回值给调用方， 第二调用方通过send方式返回值给gen
    return 'suki'


if __name__ == "__main__":
    # 协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration as e:
        print(e)
    print(inspect.getgeneratorstate(gen))
