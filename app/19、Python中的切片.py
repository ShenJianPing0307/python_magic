def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a[0:3])

    s = slice(0, 3, 1) # start、stop、step
    print(a[s])


if __name__ == '__main__':
    main()
