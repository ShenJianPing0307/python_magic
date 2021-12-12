def main():
    a = {"username": "zhangsan"}
    b = {"age": 20}

    c = dict()
    c.update(a)
    c.update(b)
    print(c)
    a["username"] = "lisi"
    print(c)


from collections import ChainMap


def main2():
    a = {"username": "zhangsan"}
    b = {"age": 20}
    c = ChainMap(a, b)
    print(c)
    a["username"] = "lisi"
    print(c)


if __name__ == '__main__':
    main2()
