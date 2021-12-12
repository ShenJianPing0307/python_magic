from functools import lru_cache


@lru_cache()
def cal_func(x, y):
    print("计算函数...")
    res = x * y + x / y
    return res


def main():
    print(cal_func(10, 2))
    print(cal_func(10, 2))


if __name__ == '__main__':
    main()
