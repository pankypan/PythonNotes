# 不使用 yield from
final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


if __name__ == "__main__":
    my_gen = sales_sum("bobby牌手机")
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1500)
    my_gen.send(3000)
    try:
        my_gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)


