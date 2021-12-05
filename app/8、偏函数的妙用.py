from functools import partial

def connect_str(str1, str2):
    return "{}{}".format(str1, str2)


def main():
    """
    abc + hello
    bcd + hello
    :return:
    """
    # res = connect_str("abc", "hello")
    # res1 = connect_str("bcd", "hello")
    #
    # print(res)
    # print(res1)
    connect_str_1 = partial(connect_str, str2="hello")
    res = connect_str_1("bcd")
    print(res)




if __name__ == '__main__':
    main()
