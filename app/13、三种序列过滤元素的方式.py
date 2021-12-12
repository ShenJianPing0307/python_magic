import itertools

def main():
    """列表生成式、生成器"""
    num_list = [-1, 3, 5, 6, -2]

    num_list_1 = [i for i in num_list if i > 1]
    print(num_list_1)

    num_list_2 = (i for i in num_list if i > 1)
    print(num_list_2)
    print(next(num_list_2), num_list_2.__next__())

def filter_func(val):
    if val > 1:
        return True
    else:
        return False

def main2():
    """filter"""
    num_list = [-1, 3, 5, 6, -2]

    res = filter(filter_func, num_list)
    print(list(res))

def main3():
    """itertools.compress"""
    num_list = [-1, 3, 5, 6, -2]
    res = itertools.compress(num_list, [False, True, True, True, True])
    print(list(res))

    # 家庭成员个数序列
    person_num = [1, 5, 3]
    f = [i > 1 for i in person_num]
    print(f)


if __name__ == '__main__':
    main3()
