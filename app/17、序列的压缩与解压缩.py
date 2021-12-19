
def main():
    a = [1, 2, 3]
    b = [4, 5, 6]
    # 压缩
    print(list(zip(a, b)))

    # 解压缩
    c = [(1, 4), (2, 5), (3, 6)]
    print(list(zip(*c)))

    strs = ["flowers", "flow", "flight"]
    prefix = ""
    for i in zip(*strs):
        print(i) # (f,f,f)
        if len(set(i)) == 1:
            prefix += i[0]
    print(prefix)




if __name__ == '__main__':
    main()