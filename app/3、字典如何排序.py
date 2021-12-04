from collections import OrderedDict

def main():
    # 方式一
    d1 = {str(i):i for i in range(10)}
    print(d1)

    # 方式二
    d = OrderedDict()
    d['A'] = 'a'
    d['B'] = 'b'
    d['C'] = 'c'
    print(d)

    for k, v in d.items():
        print(k, v)



if __name__ == '__main__':
    main()