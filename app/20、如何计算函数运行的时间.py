import time
import timeit

def wrapper(func):
    def inner(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return inner

@wrapper
def func():
    time.sleep(2)


def func1():
    time.sleep(1)


def main():
    # start = time.time()
    # func()
    # end = time.time()
    # print(end - start)
    # func1()
    # func()
    res = timeit.timeit(func1, number=2)
    print(res)


if __name__ == '__main__':
    main()
